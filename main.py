import json
from pathlib import Path


def calculer_parts(situation: str, enfants: int) -> float:
    situation = situation.lower()
    if situation in ["marié", "pacsé"]:
        parts = 2
    else:  # célibataire ou veuf
        parts = 1

    if enfants == 1:
        parts += 0.5
    elif enfants == 2:
        parts += 1
    elif enfants >= 3:
        parts += 1 + (enfants - 2)

    return parts


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


def sauvegarder_infos(nom: str, age: int, situation: str, enfants: int, fichier="data/utilisateurs.json"):
    chemin = chemin_fichier(fichier)
    data = charger_donnees(fichier)

    data[nom] = {
        "age": age,
        "situation": situation,
        "enfants": enfants,
        "parts": calculer_parts(situation, enfants)
    }

    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return chemin


def creer_utilisateur():
    print("\n=== Création d'un nouvel utilisateur ===")
    nom = input("Entrez votre nom : ").strip() or "Inconnu"

    while True:
        try:
            age = int(input("Entrez votre âge : "))
            if age > 0:
                break
        except ValueError:
            pass
        print("⚠️ Veuillez entrer un âge valide.")

    situations = {"1": "célibataire", "2": "marié", "3": "pacsé", "4": "veuf"}
    print("\nSituation familiale :")
    for k, v in situations.items():
        print(f"{k}. {v}")
    choix = input("Votre choix (1-4) : ").strip()
    situation = situations.get(choix, "célibataire")

    while True:
        try:
            enfants = int(input("Nombre d’enfants à charge : "))
            if enfants >= 0:
                break
        except ValueError:
            pass
        print("⚠️ Veuillez entrer un nombre valide (0 ou plus).")

    parts = calculer_parts(situation, enfants)
    print(f"\n✅ {nom} a {parts} parts fiscales.")

    chemin = sauvegarder_infos(nom, age, situation, enfants)
    print(f"💾 Données sauvegardées dans {chemin}")


def charger_utilisateur():
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
        choix = int(input("Votre choix : "))
        if 1 <= choix <= len(noms):
            nom = noms[choix - 1]
            utilisateur = data[nom]
            print("\n--- Infos utilisateur ---")
            print(f"Nom : {nom}")
            print(f"Âge : {utilisateur['age']}")
            print(f"Situation : {utilisateur['situation']}")
            print(f"Enfants : {utilisateur['enfants']}")
            print(f"Parts fiscales : {utilisateur['parts']}")
        else:
            print("⚠️ Choix invalide.")
    except ValueError:
        print("⚠️ Entrée invalide.")


def main():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Créer un nouvel utilisateur")
        print("2. Charger un utilisateur existant")
        print("3. Quitter")

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


if __name__ == "__main__":
    main()
2