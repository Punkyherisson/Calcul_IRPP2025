# main.py

import json
from pathlib import Path
from etat_civil import saisir_etat_civil

# 🔹 Variables globales pour l'utilisateur actif
utilisateur_actif = None
nom_utilisateur_actif = None

# 🔹 Fichier de données
DATA_FILE = Path("data/utilisateurs.json")


# -----------------------------
# Fonctions JSON
# -----------------------------
def creer_dossier_sauvegarde():
    dossier = Path("data")
    dossier.mkdir(exist_ok=True)
    return dossier


def charger_utilisateurs():
    """Charge les utilisateurs depuis le JSON."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def sauvegarder_utilisateurs(data: dict):
    """Sauvegarde les utilisateurs dans le JSON."""
    creer_dossier_sauvegarde()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# -----------------------------
# Affichage état civil
# -----------------------------
def afficher_etat_civil(utilisateur: dict, titre="État civil en cours", nom_clef=None):
    """Affiche un résumé lisible des infos état civil."""
    print(f"\n--- {titre} ---")
    nom = utilisateur.get("nom", nom_clef if nom_clef else "Inconnu")
    print(f"Nom                : {nom}")
    print(f"Année naissance    : {utilisateur.get('annee_naissance', 'N/A')}")
    if "annee_naissance_conjoint" in utilisateur:
        print(f"Conjoint né en     : {utilisateur['annee_naissance_conjoint']}")
    print(f"Situation          : {utilisateur.get('situation', 'N/A')}")
    print(f"Enfants            : {utilisateur.get('enfants', 'N/A')}")
    print(f"Parts fiscales     : {utilisateur.get('parts', 'N/A')}")
    print("---------------------------\n")


# -----------------------------
# Création utilisateur
# -----------------------------
def creer_utilisateur():
    global utilisateur_actif, nom_utilisateur_actif

    # 🔹 Saisie état civil
    infos = saisir_etat_civil()
    nom = infos["nom"]

    # 🔹 Saisie revenus
    while True:
        try:
            revenu1 = float(input("Revenu net imposable du déclarant 1 (1AJ) : "))
            break
        except ValueError:
            print("⚠️ Entrez un montant numérique valide.")

    revenu2 = 0.0
    if infos["situation"] in ["marié", "pacsé"]:
        while True:
            try:
                revenu2 = float(input("Revenu net imposable du déclarant 2 (1BJ) : "))
                break
            except ValueError:
                print("⚠️ Entrez un montant numérique valide.")

    while True:
        try:
            revenus_avant2017 = float(input("Revenus de versements effectués avant le 27/09/2017 : "))
            break
        except ValueError:
            print("⚠️ Entrez un montant numérique valide.")

    infos.update({
        "revenu_1AJ": revenu1,
        "revenu_1BJ": revenu2,
        "revenus_avant_2017": revenus_avant2017,
    })

    # 🔹 Sauvegarde JSON
    utilisateurs = charger_utilisateurs()
    utilisateurs[nom] = infos
    sauvegarder_utilisateurs(utilisateurs)

    # 🔹 Mettre à jour utilisateur actif
    utilisateur_actif = infos
    nom_utilisateur_actif = nom

    afficher_etat_civil(infos, "Nouvel état civil créé")


# -----------------------------
# Chargement utilisateur
# -----------------------------
def charger_utilisateur():
    global utilisateur_actif, nom_utilisateur_actif

    utilisateurs = charger_utilisateurs()
    if not utilisateurs:
        print("⚠️ Aucun utilisateur enregistré.")
        return

    print("\nUtilisateurs disponibles :")
    noms = list(utilisateurs.keys())
    for i, nom in enumerate(noms, 1):
        print(f"{i}. {nom}")

    try:
        choix = int(input("Choisissez un utilisateur : "))
        if 1 <= choix <= len(noms):
            nom_choisi = noms[choix - 1]
            infos = utilisateurs[nom_choisi]

            # Mettre à jour utilisateur actif
            utilisateur_actif = infos
            nom_utilisateur_actif = nom_choisi

            afficher_etat_civil(infos, "État civil chargé", nom_clef=nom_choisi)
        else:
            print("⚠️ Choix invalide.")
    except ValueError:
        print("⚠️ Entrée invalide.")


# -----------------------------
# Menu principal
# -----------------------------
def menu_principal():
    while True:
        print("\n===== Menu Principal =====")
        print("1. Créer un nouvel utilisateur")
        print("2. Charger un utilisateur existant")
        print("3. Quitter")

        # Afficher l'utilisateur actif si chargé
        if nom_utilisateur_actif:
            print(f"\n✅ Utilisateur actif : {nom_utilisateur_actif}")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            creer_utilisateur()
        elif choix == "2":
            charger_utilisateur()
        elif choix == "3":
            print("👋 Au revoir !")
            break
        else:
            print("⚠️ Choix invalide, essayez encore.")


# -----------------------------
# Entrée principale
# -----------------------------
if __name__ == "__main__":
    menu_principal()