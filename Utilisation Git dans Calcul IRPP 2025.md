Utilisation Git dans Calcul IRPP 2025

**🛠️ 1. Créer ou récupérer un projet**

  -----------------------------------------------------------------------
  **Commande**   **Description**
  -------------- --------------------------------------------------------
  git init       Crée un dépôt Git local dans le dossier courant.

  git clone      Copie un dépôt existant (ex. depuis GitHub) sur ton PC.
  \<url\>        
  -----------------------------------------------------------------------

------------------------------------------------------------------------

**✍️ 2. Travailler sur les fichiers**

  ---------------------------------------------------------------------------
  **Commande**   **Description**
  -------------- ------------------------------------------------------------
  git status     Vérifie l'état du dépôt (fichiers modifiés, suivis ou non).

  git diff       Montre les différences entre fichiers modifiés et la
                 dernière version validée.
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

**💾 3. Sauvegarder les changements**

  -----------------------------------------------------------------------
  **Commande**          **Description**
  --------------------- -------------------------------------------------
  git add \<fichier\>   Ajoute un fichier spécifique dans la *staging
                        area*.

  git add .             Ajoute **tous** les fichiers modifiés à la
                        *staging area*.

  git reset \<fichier\> Retire un fichier de la *staging area*.

  git commit -m         Sauvegarde les changements avec un message
  \"message\"           explicatif.

  git log               Affiche l'historique des commits.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

**🌿 4. Gérer les branches**

  -----------------------------------------------------------------------
  **Commande**             **Description**
  ------------------------ ----------------------------------------------
  git branch               Liste toutes les branches.

  git branch \<nom\>       Crée une nouvelle branche.

  git checkout \<branche\> Change de branche.

  git checkout -b          Crée une nouvelle branche **et** bascule
  \<branche\>              dessus.

  git merge \<branche\>    Fusionne une branche dans la branche courante.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

**☁️ 5. Collaborer avec GitHub**

  -----------------------------------------------------------------------
  **Commande**           **Description**
  ---------------------- ------------------------------------------------
  git remote -v          Liste les dépôts distants.

  git remote add origin  Lie ton dépôt local à GitHub.
  \<url\>                

  git push -u origin     Envoie la branche main vers GitHub pour la
  main                   première fois.

  git push               Envoie les commits locaux vers GitHub.

  git pull               Récupère et fusionne les changements depuis
                         GitHub.

  git fetch              Récupère les changements distants sans
                         fusionner.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

**⚠️ 6. Commandes de secours**

  ------------------------------------------------------------------------
  **Commande**   **Description**
  -------------- ---------------------------------------------------------
  git reset      Annule toutes les modifications non sauvegardées
  \--hard        (dangereux).

  git rm         Supprime un fichier du projet et de Git.
  \<fichier\>    
  ------------------------------------------------------------------------

Mettre un tag sur une version donnée

![A screen shot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.3in"
height="1.9430555555555555in"}

Parfait 👍 tu veux taguer ton commit **\"V.00 Initialisation projet\"**
(hash 72ee80e5cc028ec7cdd649f4e172c91e0e13bb9b).

Voilà comment faire étape par étape :

------------------------------------------------------------------------

**🔖 Créer un tag rétroactif sur ce commit**

1.  Depuis ton dépôt, tape :

2.  git tag -a v0.0 72ee80e5cc028ec7cdd649f4e172c91e0e13bb9b -m
    \"Version 0.0 Initialisation projet\"

👉 Ici :

- -a v0.0 → crée un tag annoté nommé v0.0.

- 72ee80e5\... → c'est le hash du commit.

- -m \"\...\" → message associé au tag.

3.  Vérifie qu'il existe bien :

git tag

**🚀 Pousser le tag sur GitHub**

- Juste ce tag :

- git push origin v0.0

- Ou bien **tous les tags d'un coup** :

git push origin \--tags

![A computer screen shot of a program AI-generated content may be
incorrect.](media/image2.png){width="6.3in"
height="3.203472222222222in"}
