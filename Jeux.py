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
# <h1> Nos jeux

# %%
"""C'est dans ce module que nous allons développer les différents jeux de notre casino. Les jeux sont sous forme de classes."""


# %%
class Roulette:
    """Comment fonctionne la roulette de notre casino? Nous avons une série de 50 nombres allant de 0 à 49. Un nombre est choisie de 
    manière aléatoire dans notre série et le joueur doit tenter de le deviner. S'il devine le bon numéro, il gagne trois fois sa mise de départ.
    S'il se trompe, on regarde si le nombre tiré au sort est de la meme couleur que celui qu'il a choisi (couleur noire pour les nombres pairs
    et couleurs rouge pour les nombres impairs). Si les deux numéros ont la meme couleur, le jouer gagne la moitié de sa mise de départ. Sinon, il
    perd sa mise."""
    def __init__(self):
        pass # Notre roulette n'a pas d'attribut particulier pour le moment
    def Lancer_la_roue(self, fond):
        ## Le paramètre fond correspond à l'attribut solde du joueur. Nous l'intègrerons lorsque nous ferrons l'intégration finale
        if fond >= 25: # Ici une petite précaution: le jeu ne se lance que si le fond du joueur est inférieur à 25 FCFA car sa mise doit etre supérieur ou égale à 25 FCFA
            # Générons dans un premier temps notre série de nombres
            nombres = list()
            for nombre in range(50):
                nombres.append(nombre)
            # La partie peut commencer!
            while True: # Cette boucle contient le worflow de notre jeu et ne peut s'arreter que si le joueur ne souhaites plus continuer
                while True: # On vérifie que le numéro choisi est dans la liste
                    user_choice = input("Veuillez choisir un nombre entre 0 et 49 (Vous pouvez également choisir 0 et 49 si vous voulez):")
                    user_choice = int(user_choice) # On converti le nombre choisi par le joueur en entier pour éviter de potentielles erreurs de comparaison
                    if user_choice in nombres:
                        break
                    else:
                        print("Veuillez entrer un numéro qui se trouve dans la plage donnée.")
                        continue
                while True: # On vérifie que le montant de la mise est dans les normes
                    try:
                        mise = input("Combien souhaitez-vous miser?") # Le joueur place sa mise
                        mise = int(mise) # On converti également la mise pour éviter les erreurs
                        assert mise >= 25 # On vérifie que sq mise est bien supérieur à 25 FCFA
                        break
                    except AssertionError: # Si sa mise est inférieur à 25FCFA, on lui de redemande d'entrer une mise valide
                        print("Votre mise doit etre supérieur ou égale à 25 FCFA")
                        continue
                fond -= mise # On déduit la mise du fond du joueur et on le lui affiche
                print("Votre fond est à présent de {} FCFA".format(fond))
                # On lance la roue!
                from random import choice # La fonction choice() va choisir un nombre au hasard dans notre liste et nous le renvoyer
                print("Attention! On lance la roue.")
                roulette_choice = choice(nombres)
                if user_choice == roulette_choice: # Cas où le joueur à choisi le numéro gagnant
                    mise *= 3
                    print("Félications! Vous avez tirez le numéro gagnant.\n Votre mise est multipliée par trois et votre gain est de : ", mise)
                    fond += mise # On met le fond à jour et on l'affiche
                    print("Votre fond est à présent de {}".format(fond))
                    retry = input("Souhaitez-vous relancer la roue?(y pour 'oui' n pour 'non')")
                    if retry in "yY": # Cas où le joueur veut remettre ça
                        continue
                    else: # Cas où le joueur ne souhaites plus continuer
                        break
                elif roulette_choice % 2 == 0 and user_choice % 2 == 0 : # Cas où le numéro choisi par l'utilisateur et celui tiré au sort sont tous deux pairs
                    print("Le numéro gagnant était : {}. \n Il s'agit d'un numéro noir!".format(roulette_choice))
                    gain = mise/2 # On calcule le gain
                    mise += gain
                    fond += mise # On met à jour le fond
                    print("Vous avez choisis un numéro de meme couleur que le numéro gagnant. \n Votre gain est de : {}.".format(mise))
                    print("Votre fond est à présent de {}".format(fond))
                    retry = input("Souhaitez-vous relancer la roue?(y pour 'oui' n pour 'non')")
                    if retry in "yY": # Cas où le joueur veut remettre ça
                        continue
                    else: # Cas où le joueur ne souhaites plus continuer
                        break
                elif roulette_choice % 2 == 1 and user_choice % 2 == 1 : # Cas où le numéro choisi par l'utilisateur et celui tiré au sort sont tous deux impairs
                    print("Le numéro gagnant était : {}. \n Il s'agit d'un numéro rouge!".format(roulette_choice))
                    gain = mise/2 # On calcule le gain
                    mise += gain
                    fond += mise # On met à jour le fond
                    print("Vous avez choisis un numéro de meme couleur que le numéro gagnant. \n Votre gain est de : {}.".format(mise))
                    print("Votre fond est à présent de {}".format(fond))
                    retry = input("Souhaitez-vous relancer la roue?(y pour 'oui' n pour 'non')")
                    if retry in "yY": # Cas où le joueur veut remettre ça
                        continue
                    else: # Cas où le joueur ne souhaites plus continuer
                        break
                else:
                    print("Vous avez perdu!")
                    print("Le numéro gagnant était : {}.".format(roulette_choice))
                    print("Votre fond est à présent de {}".format(fond))
                    retry = input("Souhaitez-vous relancer la roue?(y pour 'oui' n pour 'non')")
                    if retry in "yY": # Cas où le joueur veut remettre ça
                        continue
                    else: # Cas où le joueur ne souhaites plus continuer
                        break
        else:
            print("Votre fond est insuffisant pour jouer à ce jeu.")
