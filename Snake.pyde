from Jeu import *
from Snake import *


# taille de la fenêtre
width, height = 720, 720



# Création du menu d'acceuil
menu = Menu()
jeu = None # Le jeu n'est pas encore créé


def setup():
    frameRate(30) # fréquence de mise à jour 30 fois par seconde
    # Application de la taille de la fenêtre
    size(width, height)
    

# variables utilitaire à la gestion des différents menu
menu_option = 0 # menu principale
jouer = False # le jeu n'est pas lancé

def draw():
    global jouer, jeu, menu_option 
    
    # Mise à jour de l'arrière plan
    background(0, 0, 220) # couleur bleu océan
    
    # Si le jeu n'est pas lancé
    if jouer == False:
        
        # Si on est sur le menu principal
        if menu_option == 0:
            # on l'affiche
            menu.afficher_principale()
            
            # Clique sur bouton "jouer"
            if menu.est_cliquer_jouer():
                # création d'un nouveau jeu avec les paramètres du menu "personnaliser"
                jeu = Jeu(width, height, menu.jeu_options) 
                jouer = True # le jeu va être lancé
            
            # Clique sur bouton "personnaliser"
            elif menu.est_cliquer_personnaliser():
                menu_option = 1 # on passe sur le menu "personnaliser"
        
        # Si on est sur le menu "personnaliser"
        elif menu_option == 1:
            # on l'affiche
            menu.afficher_personnaliser()
            
            # Clique sur bouton "jouer"
            if menu.est_cliquer_jouer_personnaliser():
                # création d'un nouveau jeu avec les paramètres du menu "personnaliser"
                jeu = Jeu(width, height, menu.jeu_options)
                jouer = True # le jeu va être lancé
    
    # Si le jeu est lancé
    else:
        # On affiche les différents éléments du jeu
        jeu.afficher()
        # Mise à jour du jeu
        jeu.update()
        
        # Si le jeu demande de retourner au menu principal
        if jeu.retour_menu():
            jouer = False # on arrête le jeu
            menu_option = 0 # on repasse sur le menu principal
