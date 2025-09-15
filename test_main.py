import os
import json
import tempfile
import pytest

from etat_civil import calculer_parts
from revenus import saisir_revenus
from main import sauvegarder_infos, charger_donnees


def test_calculer_parts():
    # Célibataire sans enfant
    assert calculer_parts("célibataire", 0) == 1
    # Marié avec 2 enfants
    assert calculer_parts("marié", 2) == 3
    # Pacsé avec 3 enfants
    assert calculer_parts("pacsé", 3) == 4
    # Divorcé avec 1 enfant
    assert calculer_parts("divorcé", 1) == 1.5


def test_sauvegarde_et_chargement():
    # Fichier JSON temporaire
    with tempfile.TemporaryDirectory() as tmpdir:
        fichier = os.path.join(tmpdir, "utilisateurs.json")

        # Données fictives
        infos = {
            "nom": "Testeur",
            "annee_naissance": 1980,
            "situation": "célibataire",
            "enfants": 1,
            "parts": 1.5,
            "revenu_1AJ": 30000.0,
            "revenus_avant_2017": 0.0,
        }

        # Sauvegarde
        chemin = sauvegarder_infos("Testeur", infos, fichier=fichier)
        assert os.path.exists(chemin)

        # Rechargement
        data = charger_donnees(fichier=fichier)
        assert "Testeur" in data
        assert data["Testeur"]["nom"] == "Testeur"
        assert data["Testeur"]["parts"] == 1.5


def test_saisir_revenus(monkeypatch):
    """
    On simule des inputs utilisateur avec monkeypatch.
    """
    inputs = iter([
        "25000",   # revenu déclarant 1
        "12000",   # revenu déclarant 2
        "1500",    # enfant 1
        "0"        # revenus avant 2017
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    utilisateur = {
        "nom": "Couple",
        "situation": "marié",
        "enfants": 1,
    }
    updated = saisir_revenus(utilisateur)

    assert updated["revenu_1AJ"] == 25000.0
    assert updated["revenu_1BJ"] == 12000.0
    assert updated["revenu_enfant_1"] == 1500.0
    assert updated["revenus_avant_2017"] == 0.0