# Calcul\_IRPP2025

📌 Projet Python pour calculer l'impôt sur le revenu 2025 (France).
Ce projet évolue progressivement par versions, en commençant par la collecte des informations de l'utilisateur et la sauvegarde dans un fichier JSON.

---

## ⚙️ Version actuelle : V0.3

### ✅ Fonctionnalités

* Menu interactif avec 3 options :

  1. Créer un nouvel utilisateur
  2. Charger un utilisateur existant
  3. Quitter
* Création d’un utilisateur :

  * Nom
  * Année de naissance
  * Situation familiale (célibataire, marié, pacsé, veuf, divorcé)
  * Année de naissance du conjoint (si marié/pacsé)
  * Nombre d’enfants à charge
  * Calcul automatique des parts fiscales
  * Revenus :

    * Revenu net imposable du déclarant 1 (1AJ)
    * Revenu net imposable du déclarant 2 (1BJ) si couple
    * Revenus de versements effectués avant le 27/09/2017
* Sauvegarde automatique des informations dans un fichier JSON (`data/utilisateurs.json`)
* Possibilité de charger un utilisateur existant et d’afficher son état civil
* Indication claire de l’**utilisateur actif** dans le menu principal

---

## 🗂️ Organisation du projet

```
Calcul_IRPP2025/
│
├── main.py              # Programme principal (menu, gestion utilisateurs)
├── etat_civil.py        # Module séparé pour la saisie de l’état civil
├── data/                # Répertoire des données
│   └── utilisateurs.json
└── README.md            # Documentation du projet
```

---

## ▶️ Utilisation

### 1. Lancer le programme

python main.py

### 2. Exemple de menu

```
===== Menu Principal =====
1. Créer un nouvel utilisateur
2. Charger un utilisateur existant
3. Quitter
```

### 3. Exemple de création d’utilisateur

```
=== Création d'un nouvel utilisateur ===
Nom : Alice
Année de naissance : 1985
Situation familiale : marié
Année de naissance du conjoint : 1983
Enfants à charge : 2
Revenu net imposable du déclarant 1 (1AJ) : 35000
Revenu net imposable du déclarant 2 (1BJ) : 25000
Revenus avant 27/09/2017 : 500

--- Nouvel état civil créé ---
Nom                : Alice
Année naissance    : 1985
Conjoint né en     : 1983
Situation          : marié
Enfants            : 2
Parts fiscales     : 3
```

---

## 🔮 Prochaines étapes (V0.4+)

* Ajouter la **prise en compte du barème progressif 2025** pour calculer l’impôt brut
* Gérer les **abattements spécifiques** (ex. revenus avant 2017, pensions, etc.)
* Générer un **résumé d’imposition** (impôt brut, décote, impôt net)
* Améliorer les tests unitaires et la validation des saisies

---

## 👨‍💻 Auteur

Projet développé par *Punkyherisson*
Version actuelle : **V0.3**

