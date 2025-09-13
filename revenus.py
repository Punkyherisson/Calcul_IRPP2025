def saisir_revenus(utilisateur: dict) -> dict:
    """
    Demande à l'utilisateur de saisir ses revenus (déclarant 1, 2, enfants).
    Les revenus saisis sont ajoutés au dictionnaire utilisateur.
    """
    print("\n=== Saisie des revenus ===")

    # Déclarant 1
    while True:
        try:
            revenu1 = float(input("Revenu net imposable du déclarant 1 (1AJ) : "))
            break
        except ValueError:
            print("⚠️ Entrez un montant numérique valide.")
    utilisateur["revenu_1AJ"] = revenu1

    # Déclarant 2 si couple
    if utilisateur.get("situation") in ["marié", "pacsé"]:
        while True:
            try:
                revenu2 = float(input("Revenu net imposable du déclarant 2 (1BJ) : "))
                break
            except ValueError:
                print("⚠️ Entrez un montant numérique valide.")
        utilisateur["revenu_1BJ"] = revenu2

    # Enfants (salaire d'apprentissage, petits jobs, etc.)
    enfants = utilisateur.get("enfants", 0)
    for i in range(1, enfants + 1):
        while True:
            try:
                revenu_enfant = float(input(f"Revenu imposable de l’enfant {i} : "))
                break
            except ValueError:
                print("⚠️ Entrez un montant numérique valide.")
        utilisateur[f"revenu_enfant_{i}"] = revenu_enfant

    # Revenus avant 27/09/2017
    while True:
        try:
            revenus_avant2017 = float(input("Revenus de versements effectués avant le 27/09/2017 : "))
            break
        except ValueError:
            print("⚠️ Entrez un montant numérique valide.")
    utilisateur["revenus_avant_2017"] = revenus_avant2017

    print("\n✅ Revenus enregistrés avec succès.\n")
    return utilisateur