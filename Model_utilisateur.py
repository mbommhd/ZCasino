#!/usr/bin/env python
# coding: utf-8

# <h1> Utilisateur

# In[1]:


"""Ici, nous allons développer notre modèle utilisateur c'est à dire les attributs de nos joueurs ainsi que les différentes actions possibles de
ces derniers dans notre casino."""


# In[2]:


from pickle import Pickler, Unpickler
import os


# In[3]:


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
        """Cette méthode créé automatiquement notre base de données dans le fichier dédié si elle n'existe pas. Si elle existe, rien du tout.
        Notre base de données est une liste dans laquelle nous ajouterons chaque nouvel utilisateur. Chaque utilisateur est représenté par un 
        dictionnaire."""
        BDU = list()
        if not os.path.exists("Bases de données utilisateurs.txt"): # Ici, notre base de données est crée seulement si elle n'existe pas
            with open("Bases de données utilisateurs.txt", "wb") as bd:
                create = Pickler(bd)
                create.dump(BDU)
            
    def _Enregistrement_de_l_utilisateur(self):
        """Cette méthode enregistre automatiquement chaque nouvel utilisateur dans la base de données. Chaque profil utilisateur est
        enregistré dans un dictionnaire."""
        # On capture le profil de l'utilisateur dans un dictionnaire
        profil = {"pseudo":self.pseudo, "pwd":self.mot_de_passe, "balance":self.solde}
        # On ouvre notre base de données et on y intègre le nouveau profil
        try:
            with open("Bases de données utilisateurs.txt", "rb") as bd:
                users_data = Unpickler(bd) # Ici, on ouvre le fichier texte qui héberge notre base de données et on charge celle ci dans BDU
                BDU = users_data.load()
        except (FileNotFoundError, EOFError):
            BDU = list() # Ici, on créer une nouvelle base de données dans le cas où elle ne n'existerait pas
        BDU.append(profil) # On ajoute le profil dans la BD
        with open("Bases de données utilisateurs.txt", "wb") as bd:
            users_data = Pickler(bd) # Ici, on met à jour notre base de données dans le fichier texte
            users_data.dump(BDU)
            
    def _Sauvegarde_solde(self):
        """Cette méthode est exécutée automatiquement pour sauvegarder le solde du joueur à chaque fois qu'il termine une partie."""
        # On récupère la base de données et on la charge dans BDU
        try:
            with open("Bases de données utilisateurs.txt", "rb") as bd:
                get_data = Unpickler(bd)
                BDU = get_data.load()
        except (FileNotFoundError, EOFError):
            return
        # On parcours ensuite la BD et met à jour le solde du joueur
        for user in BDU:
            if user["pseudo"] == self.pseudo:
                user["balance"] = self.solde
                break
        # On met à jour la base dans le fichier texte
        with open("Bases de données utilisateurs.txt", "wb") as bd:
            users_data = Pickler(bd)
            users_data.dump(BDU)

    def Changer_pseudo(self):
        """Cette méthode permet à l'utilisateur de changer son nom d'utilisateur"""
        new_pseudo = input("Entrez votre nouveau nom d'utilisateur:")
        try:
            with open("Bases de données utilisateurs.txt", "rb") as bd:
                get_data = Unpickler(bd)
                BDU = get_data.load()
        except (FileNotFoundError, EOFError):
            print("Base de données introuvable")
            return
        for user in BDU: # On parcours la base remplace l'ancien pseudo par le nouveau
            if user["pseudo"] == self.pseudo:
                user["pseudo"] = new_pseudo
                self.pseudo = new_pseudo
                break
        # Mise à jour de la base de données
        with open("Bases de données utilisateurs.txt", "wb") as bd:
            users_data = Pickler(bd)
            users_data.dump(BDU)
        print("votre nom d'utilisateur à été modifié avec succes!")

    def Changer_mot_de_passe(self):
        """Cette méthode permet à l'utilisateur de changer son mot de passe."""
        new_pwd = input("Entrez votre nouveau mot de passe(huit caractères minimum):")
        while len(new_pwd) < 8:
            print("Le mot de passe doit avoir au moins huit caractères")
            new_pwd = input("Essayer encore:")
        confirm_new_pwd = input("Confirmer le nouveau mot de passe:")
        while confirm_new_pwd != new_pwd:
            print("Veuillez entrer un mot de passe identique au précédent:")
            confirm_new_pwd = input("Confirmer à nouveau le mot de passe:")
        try:
            with open("Bases de données utilisateurs.txt", "rb") as bd:
                get_data = Unpickler(bd)
                BDU = get_data.load()
        except (FileNotFoundError, EOFError):
            print("Base de données introuvable")
            return
        for user in BDU:
            if user["pseudo"] == self.pseudo:
                user["pwd"] = new_pwd
                self.mot_de_passe = new_pwd
                break
        with open("Bases de données utilisateurs.txt", "wb") as bd:
            users_data = Pickler(bd)
            users_data.dump(BDU)
        print("votre mot de passe à été modifié avec succes!")

