#!/usr/bin/env python
"""Script pour automatiser git bisect afin de trouver le commit avec le bogue."""
import os
import sys

def main():
    """Exécute git bisect pour trouver le commit problématique."""
    
    # Récupérer les hashs des commits (bon et mauvais)
    # Si des arguments sont fournis, les utiliser
    if len(sys.argv) >= 3:
        badhash = sys.argv[1]
        goodhash = sys.argv[2]
    else:
        # Utiliser des variables d'environnement ou valeurs par défaut
        badhash = os.environ.get('BAD_COMMIT', 'HEAD')
        goodhash = os.environ.get('GOOD_COMMIT', 'HEAD~10')
    
    # Commande de test à exécuter pour chaque commit
    # Retourne 0 si le commit est bon, non-zéro si mauvais
    test_command = "python manage.py test"
    
    print(f"Démarrage du git bisect...")
    print(f"Mauvais commit: {badhash}")
    print(f"Bon commit: {goodhash}")
    
    # Démarrer git bisect avec les hashs
    os.system(f"git bisect start {badhash} {goodhash}")
    
    # Exécuter git bisect run avec la commande de test
    print(f"Exécution de git bisect run avec: {test_command}")
    exit_code = os.system(f"git bisect run {test_command}")
    
    # Réinitialiser git bisect
    os.system("git bisect reset")
    
    return exit_code

if __name__ == '__main__':
    sys.exit(main())

