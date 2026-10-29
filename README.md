# ZCasino

Petit projet de casino en Python en POO

## Description
Il s'agit d'un projet formateur qui simule un casino simple. Il permet de gérer des utilisateurs, de sauvegarder leur solde, et 
n'offre qu'un seul jeu pour le moment : la Roulette. Les gains sont purement fictifs. Ce projet a pour objectif de mettre en 
pratique les concepts clés de la POO (classes, encapsulation, persistance des données, etc.). 

## Fonctionnalités
- Création de compte utilisateur
- Connexion à un compte existant
- Gestion du solde (Chaque nouvel utilisateur reçoit un solde de 1000)
- Jeu de la roulette (Mise sur un numéro entre 0 et 49, bornes incluses)
- Gains selon le numéro exact ou la la couleur (pair/impair)
- Modification du pseudo et du mot de passe
- Sauvegarde automatique des données

## Modules
- Model_utilisateur.py: Modélise les attributs et actions possibles des joueurs, gère la base de données.
- Jeux.py: Intègre tous les jeux du casino sous forme de classes.
- ZCasino.ipynb: Workflow principal (Même si dépourvu d'interface pour le moment, notre casino en aura bientôt une d'ici la
prochaine version.)

## Pré-requis:
- Python 3.x
- Jupyter Notebook
