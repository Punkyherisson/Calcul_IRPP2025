import json
from pathlib import Path


def calculer_parts(situation: str, enfants: int) -> float:
    """
    Calcule le nombre de parts fiscales.
    - situation : 'célibataire', 'marié', 'pacsé', 'veuf'
    - enfants : nombre d'enfants à charge
    """
    situation = situation.lower()
    if situation in ["marié", "pacsé"]:
        parts = 2
    else:  # célibataire ou veuf
        parts = 1

    # Enfants
    if enfants == 1:
        parts += 0.5
    elif enfants == 2:
        parts += 1
    elif enfants >= 3:
        parts += 1 + (enfants - 2)

    return parts


def creer_dossier_sauvegarde():
    """Crée un dossier 'data' s'il n'existe pas."""
    dossier = Path("data")
    dossier.mkdir(exist_ok=True)
    return dossier


def sauvegarder_infos(nom: str, age: int, situation: str, enfants: int, fichier="data/utilisateurs.json"):
    """
    Sauvegarde les informations utilisateur dans un fichier JSON.
    Si le fichier existe déjà, ajoute ou met à jour la fiche utilisateur.
    """
    dossier = creer_dossier_sauvegarde()
    chemin = dossier / Path(fichier).name

    # Charger l'existant
    if chemin.exists():
        with open(chemin, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    # Ajouter ou mettre à jour
    data[nom] = {
        "age": age,
        "situation": situation,
        "enfants": enfants,
        "parts": calculer_parts(situation, enfants)
    }

    # Sauvegarder
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return chemin


def main():
    print("=== Saisie des informations fiscales ===")
    nom = input("Entrez votre nom : ").strip() or "Inconnu"

    # Validation âge
    while True:
        try:
            age = int(input("Entrez votre âge : "))
            if age > 0:
                break
        except ValueError:
            pass
        print("⚠️ Veuillez entrer un âge valide (nombre positif).")

    # Choix situation familiale
    situations = {
        "1": "célibataire",
        "2": "marié",
        "3": "pacsé",
        "4": "veuf"
    }
    print("\nSituation familiale :")
    for k, v in situations.items():
        print(f"{k}. {v}")
    choix = input("Votre choix (1-4) : ").strip()
    situation = situations.get(choix, "célibataire")

    # Validation enfants
    while True:
        try:
            enfants = int(input("Nombre d’enfants à charge : "))
            if enfants >= 0:
                break
        except ValueError:
            pass
        print("⚠️ Veuillez entrer un nombre valide (0 ou plus).")

    # Calcul
    parts = calculer_parts(situation, enfants)

    print("\n--- Résumé ---")
    print(f"Nom : {nom}")
    print(f"Âge : {age}")
    print(f"Situation familiale : {situation}")
    print(f"Enfants à charge : {enfants}")
    print(f"Nombre de parts fiscales : {parts}")

    # Sauvegarde dans JSON
    chemin = sauvegarder_infos(nom, age, situation, enfants)
    print(f"\n✅ Données sauvegardées dans {chemin}")


if __name__ == "__main__":
    main()