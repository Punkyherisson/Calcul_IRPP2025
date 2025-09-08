def demander_nom():
    nom = input("Entrez votre nom : ").strip()
    return nom if nom else "Inconnu"

def demander_age():
    while True:
        try:
            age = int(input("Entrez votre âge : "))
            if age > 0:
                return age
        except ValueError:
            pass
        print("⚠️ Veuillez entrer un âge valide (nombre positif).")

def demander_situation_familiale():
    situations = {
        "1": "célibataire",
        "2": "marié",
        "3": "pacsé",
        "4": "veuf"
    }
    print("Choisissez votre situation familiale :")
    for key, value in situations.items():
        print(f"{key}. {value}")
    
    choix = input("Votre choix : ").strip()
    return situations.get(choix, "célibataire")

def demander_enfants():
    while True:
        try:
            enfants = int(input("Nombre d’enfants à charge : "))
            if enfants >= 0:
                return enfants
        except ValueError:
            pass
        print("⚠️ Veuillez entrer un nombre valide (0 ou plus).")

def calculer_parts(situation, enfants):
    # Base
    if situation in ["marié", "pacsé"]:
        parts = 2
    else:  # célibataire ou veuf
        parts = 1
    
    # Enfants
    if enfants > 0:
        if enfants == 1:
            parts += 0.5
        elif enfants == 2:
            parts += 1
        else:  # 3 enfants ou plus
            parts += 1 + (enfants - 2)
    
    return parts

def main():
    nom = demander_nom()
    age = demander_age()
    situation = demander_situation_familiale()
    enfants = demander_enfants()

    parts = calculer_parts(situation, enfants)

    print("\n--- Résumé ---")
    print(f"Nom : {nom}")
    print(f"Âge : {age}")
    print(f"Situation familiale : {situation}")
    print(f"Enfants à charge : {enfants}")
    print(f"Nombre de parts fiscales : {parts}")

if __name__ == "__main__":
    main()