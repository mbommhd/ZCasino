# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# <h1>ZCasino

# %%
# C'est dans ce module que nous allons implémenter le Workflow de notre casino.
from pickle import Pickler, Unpickler
from Model_utilisateur import *
from Jeux import *

# %%
print("Connectez-vous à votre compte ou créez en un pour continuer")

# %%
login = input("Tapez \n 1 pour créer un compte \n 2 pour vous connectez à votre compte")

# %%
if login == '1': # Cas où l'utilisateur souhaite créer un compte
    pseudo = input("Entrez votre nom d'utilisateur:")
    while True:
        mdp = input("Créez un mot de passe solide(huit caractères minimum):")
        if len(mdp) >= 8:
            confirm_mdp = input("Confirmez votre mot de passe:")
            if confirm_mdp == mdp: # si l'utilisateur confirme son mot de passe, on créer un nouvel utilisateur avec les attributs pseudo et mdp
                joueur = Joueur(pseudo, mdp)
                joueur._Create_data_base() # Initialisation de la base de données.
                joueur._Enregistrement_de_l_utilisateur() # On enregistre l'utilisateur dans la base de données
                print("Votre profil a bien été créer")
                break
            else:
                print("Confirmation incorrecte! Veuillez récréer votre mot de passe.")
                continue
        else:
            print("Votre mot de passe doit faire huit caractères minimum")
            continue
elif login == '2': # Cas où l'utilisateur souhaite se connecter à son compte
    while True:
        pseudo = input("Entrez votre nom d'utilisateur:") # L'utilisateur saisi ses identifiants
        mdp = input("Entrez votre mot de passe:")
        try: # Chargement de la base de données
            with open("Bases de données utilisateurs.txt", "rb") as bd:
                get_data = Unpickler(bd)
                BDU = get_data.load()
        except (FileNotFoundError, EOFError):
            print("Base de données inexistante!")
        trouve = False
        for user in BDU: # Vérification d'une correspondance dans la BD 
            if user["pseudo"] == pseudo and user["pwd"] == mdp: # Restauration des paramètres utilisateurs en cas de correspondance
                joueur = Joueur(pseudo, mdp)
                joueur.solde = user["balance"]
                print("Bienvenue, ", pseudo)
                trouve = True
                break
        if trouve:
            break
        else:
            print("Connexion Impossible: Aucune correspondance trouvée dans la base de données. \n Il se peut que votre nom d'utilisateur \
            et/ou votre mot de passe soit incorrect.")
            reconnexion = input("Retenter la connexion(y pour oui, n pour non):")
            if reconnexion in "yY":
                continue
            else:
                break


# %%
def Menu_principal(joueur):
    while True:
        print("User: {} \n Balance: {} \n PassWord: ******** \n".format(joueur.pseudo, joueur.solde))
        print("Bienvenue dans ZCasino.\n")
        print("Liste des jeux: \n 1- La Roulette \n")
        print("Paramètres du compte: \n 1- Réinitialiser le nom d'utilisateur \n 2- Réinitialiser le mot de passe \n 3- Se Déconnecter. \n")
        print("Quitter le Casino.")

        action = input("Tapez a pour jouer à un jeu, b pour les paramètres du comptes, q pour quitter le Casino:")
        action = action.lower()

        if action == 'a': # Choix du jeu
            choice = input("A quel jeu souhaitez-vous jouer?(ex: 1 pour la Roulette):")
            if choice == '1': # Lancement du jeux de la roulette
                roue = Roulette()
                joueur.solde = roue.Lancer_la_roue(joueur.solde)
                joueur._Sauvegarde_solde()
                print("User: {} \n Balance: {} \n PassWord: ******** \n".format(joueur.pseudo, joueur.solde))
            else:
                print("Ce jeu n'est pas disponible pour le moment.")
        elif action == 'b': # Paramètres du compte
            choice = input("Tapez \n 1 pour réinitialiser le nom d'utilisateur \n 2 pour réinitialiser le mot de passe \n 3 pour se déconnecter:")
            if choice == '1':
                joueur.Changer_pseudo()
                print("User: {} \n Balance: {} \n PassWord: ******** \n".format(joueur.pseudo, joueur.solde))
            elif choice == '2':
                joueur.Changer_mot_de_passe()
                print("User: {} \n Balance: {} \n PassWord: ******** \n".format(joueur.pseudo, joueur.solde))
            elif choice == '3':
                print("A bientot {}!".format(joueur.pseudo))
                del joueur
                break
            else:
                print("Choix invalide.")
        elif action == 'q':
            print("A bientot {}!".format(joueur.pseudo))
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


# %%
Menu_principal(joueur)
