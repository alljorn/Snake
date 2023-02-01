# coding: utf-8

from random import *


class Pomme:
    """
    La classe Pomme définit une pomme destiné à être mangé par le snake (quel pauvre destin...)
    
    - Pomme(plateu)
        plateau: Plateau | Le plateau sur laquelle appartient la pomme
        
    Attributs:
        cote: int | La taille des carreaux du plateau
        couleur: tuple[int, int, int] | La couleur de la pomme
        plateau: Plateau | Le plateau sur laquelle appartient la pomme
        x: int | La position en unité sur le plateau en x
        y: int | La position en unité sur le plateau en y
    
    Méthodes:
        - get_pos(): donne la position de la pomme
        - afficher(): affiche la pomme
    """
    
    def __init__(self, plateau):
        self.cote = plateau.taille_carreau # la taille des carreaux du plateau
        self.plateau = plateau # le plateau fournit
        self.x, self.y = choice(self.plateau.get_free_position() ) # Une positions aléatoire parmis les emplacements libres
        # (note: il est possible que la pomme apparaisse sur le snake, mais ce n'est pas grave pour le déroulement du jeu, le joueur doit juste libérer la pomme de la queue du snake) (une petite vengeance de la pomme face à son destin)
        self.couleur = (255, 0, 0) # couleur rouge pomme
    
    def get_pos(self):
        """
        Donne la position de la pomme
        
        renvoie un tuple des positions x et y
        """
        return self.x, self.y
    
    def afficher(self):
        """
        Affiche la pomme
        
        ne renvoie rien
        """
        r, v, b = self.couleur # couleur rouge, vert, bleu
        fill(r, v, b) # définition de la couleur
        pos_x, pos_y = self.plateau.get_pos_of(self.x, self.y) # récupère la position en pixel de la pomme
        rect(pos_x, pos_y, self.cote, self.cote) # affichage
        

class Obstacle:
    """
    La classe Obstacle définit un obsatcle destiné à tuer le snake (il se bat pour la cause fatale de la pomme...)
    
    - Obstacle(plateu)
        plateau: Plateau | Le plateau sur laquelle appartient l'obsatcle
        
    Attributs:
        cote: int | La taille des carreaux du plateau
        couleur: tuple[int, int, int] | La couleur de l'obsatcle
        plateau: Plateau | Le plateau sur laquelle appartient l'obsatcle
        x: int | La position en unité sur le plateau en x
        y: int | La position en unité sur le plateau en y
    
    Méthodes:
        - get_pos(): donne la position de l'obsatcle
        - afficher(): affiche l'obsatcle
    """
    
    def __init__(self, plateau):
        self.cote = plateau.taille_carreau # la taille des carreaux du plateau
        self.plateau = plateau # le plateau fournit
        self.x, self.y = choice(self.plateau.get_free_position() ) # Une positions aléatoire parmis les emplacements libres
        self.couleur = (0, 0, 0) # couleur noir
    
    def get_pos(self):
        """
        Donne la position de l'obsatcle
        
        renvoie un tuple des positions x et y
        """
        return self.x, self.y
    
    def afficher(self):
        """
        Affiche l'obsatcle
        
        ne renvoie rien
        """
        r, v, b = self.couleur # couleur rouge, vert, bleu
        fill(r, v, b) # définition de la couleur
        pos_x, pos_y = self.plateau.get_pos_of(self.x, self.y) # récupère la position en pixel de l'obsatcle
        rect(pos_x, pos_y, self.cote, self.cote) # affichage
