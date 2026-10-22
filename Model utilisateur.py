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
# <h1> Utilisateur

# %%
"""Ici, nous allons développer notre modèle utilisateur c'est à dire les attributs de nos joueurs ainsi que les différentes actions possibles de
ces derniers dans notre casino."""


# %%
class Joueur:
    """Cette classe modélise les différents attributs et actions des joueurs dans notre casino. Ces attributs et actions ne sont pas
    définitifs. Ils pourront évoluer avec le temps. 
    Les attributs de nos joueurs sont:
    -pseudo;
    -mot de passe;
    -solde
    Les actions de nos utilisateurs sont:
    -Changer de pseudo
    -Changer de mot de passe
    """
    def __init__(self, pseudo, pwd):
        self.pseudo = pseudo
        self.mot_de_passe = pwd
        self.solde = 1000 # Tous les nouveaux utilisateurs débutent avec un solde de 1000 FCFA

    def _Create_data_base(self):
        """Cette méthode créé automatiquement notre base de données dans le fichier dédié. Elle doit etre appeler une seule et unique fois. 
        Si elle est appelée plus d'une fois, toutes les données utilisateur seront perdues!"""
        from pickle import Pickler
        BDU = list() # Notre base de données est une liste dans laquelle nous ajouterons chaque nouvel utilisateur. Notre liste est ensuite sauvegardée
        # dans un fichier texte dédié
        with open("Bases de données utilisateurs.txt", "wb") as bd:
            create = Pickler(bd)
            create.dump(BDU)
            
    def _Enregistrement_de_l_utilisateur(self):
        """Cette méthode enregistre automatiquement chaque nouvel utilisateur dans la base de données"""
        from pickle import Unpickler
        # On capture le profil de l'utilisateur dans un dictionnaire
        profil = {"pseudo":self.pseudo, "pwd":self.mot_de_passe, "balance":self.solde}
        # On ouvre notre base de données et on y intègre le nouveau profil
        with open("Bases de données utilisateurs.txt", "ab") as bd:
            get_data = Unpickler(bd)
            BDU = get_data.load()
            BDU.append(profil)
            
    def _Sauvegarde_solde(self):
        """Cette méthode est exécutée automatiquement pour sauvegarder le solde du joueur à chaque fois qu'il termine une partie."""
        from pickle import Unpickler
        # On ouvre la base de données et on met à jour le solde su client
        with open("Bases de données utilisateurs.txt", "ab") as bd:
            get_data = Unpickler(bd)
            BDU = get_data.load()
            # On parcours ensuite la BD et met à jour le solde du joueur
            for user in BDU:
                if user["pseudo"] == self.pseudo:
                    user["balance"] = self.solde

    def Changer_pseudo(self):
        """Cette méthode permet à l'utilisateur de changer son nom d'utilisateur"""
        from pickle import Unpickler
        new_pseudo = input("Entrez votre nouveau nom d'utilisateur:")
        with open("Bases de données utilisateurs.txt", "ab") as bd:
            get_data = Unpickler(bd)
            BDU = get_data.load()
            for user in BDU:
                if user["pseudo"] == self.pseudo:
                    user["pseudo"] = new_pseudo

    def Changer_mot_de_passe(self):
        """Cette méthode permet à l'utilisateur de changer son mot de passe."""
        from pickle import Unpickler
        new_pwd = input("Entrez votre nouveau mot de passe(huit caractères minimum):")
        while True:
            if len(new_pwd) >= 8:
                break
            else:
                print("Le mot de passe doit avoir huit caractères miinimum!")
                new_pwd = input("Essayer encore:")
                continue
        confirm_new_pwd = input("Confirmer le nouveau mot de passe:")
        while True:
            if new_pwd == confirm_new_pwd:
                break
            else:
                print("Incorrect! Veuillez réssayer")
                continue
        with open("Bases de données utilisateurs.txt", "ab") as bd:
            get_data = Unpickler(bd)
            BDU = get_data.load()
            for user in BDU:
                if user["pseudo"] == self.pseudo:
                    user["pwd"] = confirm_new_pwd
