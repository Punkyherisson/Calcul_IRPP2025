# 📌 Calcul IRPP 2025 – v0.4  

## 📖 Description  
Ce projet a pour but de **simuler le calcul de l’impôt sur le revenu en France (IRPP 2025)**.  
Il évolue étape par étape :  
- **V0.1** : Saisie simple des informations utilisateur.  
- **V0.2** : Sauvegarde et chargement des utilisateurs via fichier JSON.  
- **V0.3** : Séparation des responsabilités (`etat_civil.py`), gestion d’un utilisateur actif, affichage clair de l’état civil.  
- **V0.4** : Ajout de la saisie des revenus salariaux (cases 1AJ, 1BJ, 1CJ, 1DJ) via `revenus.py`.  

---

## ⚙️ Fonctionnalités actuelles  
- Menu interactif :  
  - Créer un utilisateur.  
  - Charger un utilisateur existant.  
  - Afficher l’utilisateur actif.  
  - Calculer l’impôt (placeholder, à implémenter).  
  - Saisir les revenus salariaux (1AJ → 1DJ).  
- Sauvegarde automatique dans un fichier **`data/utilisateurs.json`**.  
- Gestion multi-utilisateurs (plusieurs fiches sauvegardées).  

---

## 📂 Organisation du projet  
Calcul_IRPP2025/
│
├── main.py # Menu principal
├── etat_civil.py # Gestion état civil et parts fiscales
├── revenus.py # Gestion de la saisie des revenus (1AJ–1DJ)
├── tests/ # (optionnel) Fichiers de test avec pytest
│ └── test_revenus.py
│
├── data/
│ └── utilisateurs.json # Sauvegardes utilisateurs
│
└── README.md # Documentation du projet


---

## 🖥️ Exemple d’utilisation  

### 1. Lancer le programme  
python main.py

2. Menu principal
===== Menu Principal =====
1. Créer un nouvel utilisateur
2. Charger un utilisateur existant
3. Afficher l’utilisateur actif
4. Calculer l'impôt (utilisateur actif)
5. Saisir les revenus salariaux
6. Quitter

3. Exemple saisie revenus
=== Saisie des revenus salariaux ===
Salaires déclarant 1 (1AJ) : 68401
Salaires déclarant 2 (1BJ) : 3088
Salaires personne à charge 1 (1CJ) : 16380
Salaires personne à charge 2 (1DJ) : 84

--- Revenus saisis ---
1AJ : 68401.00 €
1BJ : 3088.00 €
1CJ : 16380.00 €
1DJ : 84.00 €
----------------------

✅ Prochaines étapes

Implémenter le calcul de l’impôt en fonction des revenus et parts fiscales.

Ajouter d’autres sources de revenus (fonciers, BIC/BNC, etc.).

Intégrer les barèmes IRPP 2025.

Ajouter des tests unitaires (pytest).