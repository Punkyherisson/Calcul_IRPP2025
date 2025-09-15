🔹 Python

__pycache__/ → dossier auto-généré quand Python exécute ton code (fichiers compilés .pyc).

*.pyc, *.pyo, *.pyd → fichiers Python compilés (bytecode, optimisés ou extensions).

*.pdb → fichiers de débogage Python.

*.egg-info/, *.egg → fichiers générés par l’installation de paquets Python.

🔹 Environnements virtuels

.venv/, venv/, env/, ENV/ → dossiers d’environnements virtuels contenant toutes les dépendances installées localement (tu n’as pas besoin de les mettre dans Git, il vaut mieux garder un requirements.txt).

🔹 Éditeurs et IDE

.vscode/ → paramètres spécifiques à Visual Studio Code.

.idea/ → paramètres spécifiques à PyCharm/IntelliJ.

*.swp, *.swo → fichiers temporaires créés par l’éditeur Vim.

🔹 Tests et couverture

.pytest_cache/ → cache généré par pytest.

.coverage, htmlcov/ → fichiers de rapports de couverture de tests.

.tox/, .nox/ → environnements créés par les outils de tests tox ou nox.

.mypy_cache/ → cache utilisé par mypy (vérification de types).

.cache/ → cache générique de divers outils Python.

🔹 Logs

*.log → fichiers journaux (logs d’exécution, erreurs, etc.).

🔹 OS spécifiques

.DS_Store, .AppleDouble, .LSOverride → fichiers créés automatiquement par macOS.

Thumbs.db, ehthumbs.db, Desktop.ini → fichiers créés automatiquement par Windows.

🔹 Sauvegardes

*.bak, *.tmp, *.old → fichiers de sauvegarde ou temporaires.

🔹 Spécifique projet

/data/*.json → j’ai mis cette règle pour éviter de versionner tes sauvegardes utilisateurs (qui changent souvent).