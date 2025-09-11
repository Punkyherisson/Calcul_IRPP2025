# etat_civil.py

def calculer_parts(situation: str, enfants: int) -> float:
    situation = situation.lower()
    if situation in ["marié", "pacsé"]:
        parts = 2
    else:  # célibataire, veuf, divorcé
        parts = 1

    if enfants == 1:
        parts += 0.5
    elif enfants == 2:
        parts += 1
    elif enfants >= 3:
        parts += 1 + (enfants - 2)

    return parts


def saisir_etat_civil():
    """Demande à l’utilisateur les infos d’état civil et renvoie un dict"""
    nom = input("Entrez votre nom : ").strip() or "Inconnu"

    while True:
        try:
            annee_naissance = int(input("Entrez votre année de naissance (AAAA) : "))
            if 1900 <= annee_naissance <= 2100:
                break
        except ValueError:
            pass
        print("⚠️ Veuillez entrer une année valide (ex : 1985).")

    situations = {
        "1": "célibataire",
        "2": "marié",
        "3": "pacsé",
        "4": "veuf",
        "5": "divorcé"
    }
    print("\nSituation familiale :")
    for k, v in situations.items():
        print(f"{k}. {v}")
    choix = input("Votre choix (1-5) : ").strip()
    situation = situations.get(choix, "célibataire")

    annee_naissance2 = None
    if situation in ["marié", "pacsé"]:
        while True:
            try:
                annee_naissance2 = int(input("Entrez l'année de naissance du 2ème déclarant : "))
                if 1900 <= annee_naissance2 <= 2100:
                    break
            except ValueError:
                pass
            print("⚠️ Veuillez entrer une année valide (ex : 1990).")

    while True:
        try:
            enfants = int(input("Nombre d’enfants à charge : "))
            if enfants >= 0:
                break
        except ValueError:
            print("⚠️ Veuillez entrer un nombre valide (0 ou plus).")

    parts = calculer_parts(situation, enfants)

    infos = {
        "nom": nom,
        "annee_naissance": annee_naissance,
        "situation": situation,
        "enfants": enfants,
        "parts": parts,
    }
    if annee_naissance2:
        infos["annee_naissance_conjoint"] = annee_naissance2

    return infos