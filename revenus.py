def saisir_revenus(utilisateur: dict) -> dict:
    """
    Saisie des revenus salariaux (1AJ, 1BJ, 1CJ, 1DJ).
    Met à jour le dictionnaire utilisateur et le retourne.
    """

    print("\n=== Saisie des revenus salariaux ===")
    revenus = {}

    def demander_revenu(case, description):
        while True:
            try:
                valeur = input(f"{description} ({case}) : ").strip()
                return float(valeur) if valeur else 0.0
            except ValueError:
                print("⚠️ Entrez un montant numérique valide.")

    revenus["1AJ"] = demander_revenu("1AJ", "Salaires déclarant 1")
    revenus["1BJ"] = demander_revenu("1BJ", "Salaires déclarant 2")
    revenus["1CJ"] = demander_revenu("1CJ", "Salaires personne à charge 1")
    revenus["1DJ"] = demander_revenu("1DJ", "Salaires personne à charge 2")

    utilisateur["revenus"] = revenus
    return utilisateur


def afficher_revenus(utilisateur: dict):
    """
    Affiche les revenus si disponibles.
    """
    revenus = utilisateur.get("revenus")
    if not revenus:
        print("⚠️ Aucun revenu saisi.")
        return

    print("\n--- Revenus saisis ---")
    for case, montant in revenus.items():
        print(f"{case} : {montant:.2f} €")
    print("----------------------")