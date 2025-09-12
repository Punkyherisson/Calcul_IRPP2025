import json
from pathlib import Path
from etat_civil import saisir_etat_civil, afficher_etat_civil

# Variable globale : utilisateur actuellement chargé
utilisateur_actif = None


def creer_dossier_sauvegarde():
    dossier = Path("data")
    dossier.mkdir(exist_ok=True)
    return dossier


def chemin_fichier(fichier="data/utilisateurs.json") -> Path:
    dossier = creer_dossier_sauvegarde()
    return dossier / Path(fichier).name


def charger_donnees(fichier="data/utilisateurs.json"):
    chemin = chemin_fichier(fichier)
    if chemin.exists():
        with open(chemin, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def sauvegarder_infos(nom: str, infos: dict, fichier="data/utilisateurs.json"):
    chemin = chemin_fichier(fichier)
    data = charger_donnees(fichier)

    # On s’assure que la clé "nom" existe
    infos["nom"] = nom

    data[nom] = infos

    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return chemin


def creer_utilisateur():
    global utilisateur_actif
    infos = saisir_etat_civil()
    nom = infos.get("nom", "Inconnu")
    chemin = sauvegarder_infos(nom, infos)
    utilisateur_actif = infos
    print(f"\n💾 Données sauvegardées dans {chemin}")
    afficher_etat_civil(infos, "Nouvel état civil créé")


def charger_utilisateur():
    global utilisateur_actif
    print("\n=== Charger un utilisateur existant ===")
    data = charger_donnees()

    if not data:
        print("⚠️ Aucun utilisateur enregistré. Créez-en un d'abord.")
        return

    print("Utilisateurs disponibles :")
    noms = list(data.keys())
    for i, nom in enumerate(noms, 1):
        print(f"{i}. {nom}")

    try:
        choix = int(input("Choisissez un utilisateur : "))
        if 1 <= choix <= len(noms):
            nom = noms[choix - 1]
            utilisateur_actif = data[nom]
            afficher_etat_civil(utilisateur_actif, "État civil chargé")
        else:
            print("⚠️ Choix invalide.")
    except ValueError:
        print("⚠️ Entrée invalide.")


def calcul_impot(utilisateur: dict):
    """Prototype de calcul d'impôt - à compléter"""
    print("\n=== Calcul de l'impôt ===")
    nom = utilisateur.get("nom", "Inconnu")
    revenu1 = utilisateur.get("revenu_1AJ", 0.0)
    revenu2 = utilisateur.get("revenu_1BJ", 0.0)
    parts = utilisateur.get("parts", 1)

    revenu_total = revenu1 + revenu2
    revenu_imposable = revenu_total / parts

    print(f"Contribuable : {nom}")
    print(f"Revenu total : {revenu_total} €")
    print(f"Nombre de parts : {parts}")
    print(f"Revenu imposable par part : {revenu_imposable:.2f} €")

    # Pour l'instant : pas de barème appliqué
    print("⚠️ Le calcul complet du barème n'est pas encore implémenté.")


def menu_principal():
    global utilisateur_actif
    while True:
        print("\n===== Menu Principal =====")
        print("1. Créer un nouvel utilisateur")
        print("2. Charger un utilisateur existant")
        print("3. Quitter")
        if utilisateur_actif:
            print("4. Calculer l'impôt (utilisateur actif)")
            print(f"👉 Utilisateur actif : {utilisateur_actif.get('nom', 'Inconnu')}")

        choix = input("Votre choix : ")

        if choix == "1":
            creer_utilisateur()
        elif choix == "2":
            charger_utilisateur()
        elif choix == "3":
            print("Au revoir 👋")
            break
        elif choix == "4" and utilisateur_actif:
            calcul_impot(utilisateur_actif)
        else:
            print("❌ Choix invalide.")


if __name__ == "__main__":
    menu_principal()