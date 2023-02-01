# coding: utf-8

from Snake import *
from Objets import *

import math
from random import *


class Menu:
    """
    La classe Menu s'occupe d'afficher les différents menu disponnible parmis:
        o le menu principal
        o le menu "personnaliser"
    
    - Menu()
    
    Attributs:
        jouer_angle: int | L'angle en degrés du texte "Jouer" qui tourne autour de la souris de l'utilisateur
        jeu_options: dict = { "taille": 30,
                              "vitesse": 0.1,
                              "vie": 1,
                              "obstacle": False,
                              "score_x4": False,
                              "fun": False      }
        | Les différents paramètres du jeu
    
    Méthodes:
        - afficher_personnaliser(): affiche les différents éléments du menu "Personnaliser" et gère les changements de paramètres au clique sur les boutons dédiés
        - afficher_principale(): affiche les différents éléments du menu principal
        - fun(): donne le paramètre de l'activation du mode fun
        - est_cliquer_jouer(): vérifie que le bouton "Jouer" du menu principal est cliqué
        - est_cliquer_jouer_personnaliser(): vérifie que le bouton "Jouer" du menu "Personnalisé" est cliqué
        - est_cliquer_personnaliser(): vérifie que le bouton "Personnalisé" du menu principal est cliqué
        - obstacle(): donne le paramètre de l'activation des obstacles
        - score_x4(): donne le paramètre de l'activation du multiplicateur de score
        - vitesse_niveau(): donne le paramètre de vitesse sous forme de chaine de caractère:
        - vie(): donne le paramètre du nombre de vies
    """
    
    def __init__(self):
        self.jouer_angle = 0 # L'angle en degrés du texte "Jouer" qui tourne autour de la souris de l'utilisateur
        
        # Les différents paramètres du jeu
        self.jeu_options = {"taille": 30,
                            "vitesse": 0.1,
                            "vie": 1,
                            "obstacle": False,
                            "score_x4": False,
                            "fun": False
        }
        
    def est_cliquer_jouer(self):
        """
        Vérifie que le bouton "Jouer" du menu principal est cliqué
        
        renvoie True si le bouton est cliqué, False sinon
        """
        return mousePressed and mouseX >= width/2 - 60*2.5 and mouseY >= height - height/3 - 30 and mouseX <= width/2 - 60*2.5 + 60*5 and mouseY <= height - height/3 - 30 + 60
    
    def est_cliquer_personnaliser(self):
        """
        Vérifie que le bouton "Personnalisé" du menu principal est cliqué
        
        renvoie True si le bouton est cliqué, False sinon
        """
        return mousePressed and mouseX >= width/2 - 60*2.5 and mouseY >= height - height/3 + 45 and mouseX <= width/2 - 60*2.5 + 60*5 and mouseY <= height - height/3 + 45 + 60
    
    def est_cliquer_jouer_personnaliser(self):
        """
        Vérifie que le bouton "Jouer" du menu "Personnalisé" est cliqué
        
        renvoie True si le bouton est cliqué, False sinon
        """
        return mousePressed and mouseX >= width/2 - 60*2.5 and mouseY >= height - height/7 and mouseX <= width/2 - 60*2.5 + 60*5 and mouseY <= height - height/7 + 60
    
    
    def afficher_principale(self):
        """
        Affiche les différents éléments du menu principal
        
        ne renvoie rien
        """
      ### Titre "SNAKE"
        fill(255, 255, 255) # couleur blanc
        textSize(60) # taille du texte
        textAlign(CENTER) # écriture en mode centré
        text("SNAKE", width/2, height/3) # affichage relative aux dimensions de la fenêtre
        
      ### Bouton "Personnaliser"
        # zone de clique
        fill(self.jouer_angle//2, self.jouer_angle//3, self.jouer_angle//1.5) # utilisation de l'angle du texte "Jouer" pour changer dynamiquement la couleur du bouton 
        rect(width/2 - 60*2.5, height - height/3 + 45, 60*5, 60, 20) # affichage du bouton relative aux dimensions de la fenêtre
        # texte
        fill(255,255,255) # couleur blanche
        text_size = 40
        textSize(text_size) # taille du texte
        text("Personnaliser", width/2, height - height/3+ 45*2 + text_size/10) # affichage relative aux dimensions de la fenêtre et à la taille du texte
        
      ### Bouton "Jouer"
        # zone de clique
        fill(200, 100, 0) # couleur orange
        rect(width/2 - 60*2.5, height - height/3 - 30, 60*5, 60, 20) # affichage du bouton relative aux dimensions de la fenêtre
        # texte
        fill(255,255,255) # couleur blanche
        textSize(60) # taille du texte
        translate(mouseX, mouseY) # positions sur le curseur de la souris
        rotate(math.radians(self.jouer_angle)) # tourne le texte
        text("Jouer", 0, 0) # affiche le texte
        # mise à jour de l'angle
        self.jouer_angle += 1
        if self.jouer_angle == 360:
            self.jouer_angle = 0
        
        
    def afficher_personnaliser(self):
        """
        Affiche les différents éléments du menu "Personnaliser" et gère les changements de paramètres au clique sur les boutons dédiés
        
        ne renvoie rien
        """
      ### Titre "Personnalisation"
        fill(255, 255, 255) # couleur blanc
        textSize(60) # taille du texte
        textAlign(CENTER) # écriture en mode centré
        text("Personnalisation", width/2, height/5) # affichage relative aux dimensions de la fenêtre
        
        textSize(40) # taille du texte
        
      ### Paramètre "vitesse"
        # texte
        fill(255, 255, 255) # couleur blanc
        text("vitesse: ", width/2-250, height/2.5) # affichage relative aux dimensions de la fenêtre
        # boutons
        fill(220, 220, 220) # couleur gris clair
        rect(width/2-100 - 40, height/2.5 - 40, 40*2, 45, 20) # bouton "lent"
        rect(width/2+25 - 75, height/2.5 - 40, 40*3.75, 45, 20) # bouton "normal"
        rect(width/2+175 - 65, height/2.5 - 40, 40*3.25, 45, 20) # bouton "rapide"
        
        # On récupère le paramètre de vitesse
        vitesse = self.vitesse_niveau()
        
        # Si le paramètre est "lent"
        if vitesse == "lent":
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("lent", width/2-100, height/2.5) # affichage relative aux dimensions de la fenêtre
        
        # Si le paramètre est "normal"
        if vitesse == "normal":
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("normal", width/2+25, height/2.5) # affichage relative aux dimensions de la fenêtre
        
        # Si le paramètre est "rapide"
        if vitesse == "rapide":
            fill(255, 255, 255)
        else: fill(0, 0, 0)
        text("rapide", width/2+175, height/2.5) # affichage relative aux dimensions de la fenêtre
        
        # Détections des cliques sur les boutons
        if mousePressed and mouseX >= width/2-100 - 40 and mouseX <= width/2-100 - 40 + 40*2 and mouseY >= height/2.5 - 40 and mouseY <= height/2.5 - 40 + 45: # bouton "lent"
            self.jeu_options["vitesse"] = 0.2 # Vitesse plus lente
        elif mousePressed and mouseX >= width/2+25 - 75 and mouseX <= width/2+25 - 75 +  40*3.75 and mouseY >=height/2.5 - 40 and mouseY <= height/2.5 - 40 + 45: # bouton "normal"
            self.jeu_options["vitesse"] = 0.1 # Vitesse par défaut
        elif mousePressed and mouseX >= width/2+175 - 65 and mouseX <= width/2+175 - 65 + 40*3.25 and mouseY >= height/2.5 - 40 and mouseY <= height/2.5 - 40 + 45: # bouton "rapide"
            self.jeu_options["vitesse"] = 0.05 # Vitesse plus rapide
        
      ### Paramètre "vies"
        # texte
        fill(255, 255, 255) # couleur blanc
        text("vies: ", width/2-250, height/2) # affichage relative aux dimensions de la fenêtre
        # boutons
        fill(220, 220, 220) # couleur gris clair
        rect(width/2-100 - 40, height/2 - 40, 40*2, 45, 20) # bouton "1"
        rect(width/2+25 - 75, height/2 - 40, 40*2, 45, 20) # bouton "2"
        rect(width/2+25 + 15, height/2 - 40, 40*2, 45, 20) # bouton "3"
        
        # On récupère le paramètre du nombre de vies
        vie = self.vie()
        
        # Si le paramètre est "1"
        if vie == 1:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("1", width/2-100, height/2) # affichage relative aux dimensions de la fenêtre
        
        # Si le paramètre est "2"
        if vie == 2:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("2", width/2+25 - 35, height/2) # affichage relative aux dimensions de la fenêtre
        
        # Si le paramètre est "3"
        if vie == 3:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("3", width/2+25 + 55, height/2) # affichage relative aux dimensions de la fenêtre
        
         # Détections des cliques sur les boutons
        if mousePressed and mouseX >= width/2-100 - 40 and mouseX <= width/2-100 - 40 + 40*2 and mouseY >= height/2 - 40 and mouseY <= height/2 - 40 + 45: # bouton "1"
            self.jeu_options["vie"] = 1 # Vie est maintenant égale à 1
        elif mousePressed and mouseX >= width/2+25 - 75 and mouseX <= width/2+25 - 75 +  40*2 and mouseY >=height/2 - 40 and mouseY <= height/2 - 40 + 45: # bouton "2"
            self.jeu_options["vie"] = 2 # Vie est maintenant égale à 2
        elif mousePressed and mouseX >= width/2+25 + 15 and mouseX <= width/2+25 + 15 +  40*2 and mouseY >=height/2 - 40 and mouseY <= height/2 - 40 + 45: # bouton "3"
            self.jeu_options["vie"] = 3 # Vie est maintenant égale à 3
        
      ### Paramètre "obstacles"
        # texte
        fill(255, 255, 255) # couleur blanc
        text("obstacles: ", width/2-250, height/1.65) # affichage relative aux dimensions de la fenêtre
        # boutons
        fill(220, 220, 220) # couleur gris clair
        rect(width/2-100 - 40, height/1.65 - 40, 40*2, 45, 20) # bouton "oui"
        rect(width/2+25 - 75, height/1.65 - 40, 40*2, 45, 20) # bouton "non"
        
        # On récupère le paramètre d'activation des obstacles
        obstacle = self.obstacle()
        
        # Si le paramètre est "oui"
        if obstacle:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("oui", width/2-100, height/1.65) # affichage relative aux dimensions de la fenêtre
        
        # Si le paramètre est "non"
        if not obstacle:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("non", width/2+25 - 35, height/1.65) # affichage relative aux dimensions de la fenêtre
        
        # Détections des cliques sur les boutons
        if mousePressed and mouseX >= width/2-100 - 40 and mouseX <= width/2-100 - 40 + 40*2 and mouseY >= height/1.65 - 40 and mouseY <= height/1.65 - 40 + 45: # bouton "oui"
            self.jeu_options["obstacle"] = True # Activation des obstacles
        elif mousePressed and mouseX >= width/2+25 - 75 and mouseX <= width/2+25 - 75 +  40*2 and mouseY >=height/1.65 - 40 and mouseY <= height/1.65 - 40 + 45: # bouton "non"
            self.jeu_options["obstacle"] = False # Désactivation des obstacles
        
      ### Paramètre "score x4"
        # texte
        fill(255, 255, 255) # couleur blanc
        text("score x4: ", width/2-250, height/1.45) # affichage relative aux dimensions de la fenêtre
        # boutons
        fill(220, 220, 220) # couleur gris clair
        rect(width/2-100 - 40, height/1.45 - 40, 40*2, 45, 20) # bouton "oui"
        rect(width/2+25 - 75, height/1.45 - 40, 40*2, 45, 20) # bouton "non"
        
        # On récupère le paramètre d'activation du muliplicateur de score
        score = self.score_x4()
        
        # Si le paramètre est "oui"
        if score:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("oui", width/2-100, height/1.46) # affichage relative aux dimensions de la fenêtre
        
        # Si le paramètre est "non"
        if not score:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("non", width/2+25 - 35, height/1.46) # affichage relative aux dimensions de la fenêtre
        
        # Détections des cliques sur les boutons
        if mousePressed and mouseX >= width/2-100 - 40 and mouseX <= width/2-100 - 40 + 40*2 and mouseY >= height/1.45 - 40 and mouseY <= height/1.45 - 40 + 45: # bouton "oui"
            self.jeu_options["score_x4"] = True # Activation du muliplicateur de score
        elif mousePressed and mouseX >= width/2+25 - 75 and mouseX <= width/2+25 - 75 +  40*3.75 and mouseY >=height/1.45 - 40 and mouseY <= height/1.45 - 40 + 45: # bouton "non"
            self.jeu_options["score_x4"] = False # Désactivation du muliplicateur de score
        
      ### Paramètre fun"
        # texte
        fill(255, 255, 255) # couleur blanc
        text("fun: ", width/2-250, height/1.3) # affichage relative aux dimensions de la fenêtre
        # boutons
        fill(220, 220, 220) # couleur gris clair
        rect(width/2-100 - 40, height/1.3 - 40, 40*2, 45, 20) # bouton "oui"
        rect(width/2+25 - 75, height/1.3 - 40, 40*2, 45, 20) # bouton "non"
        
        # On récupère le paramètre d'activation du mode fun
        fun = self.fun()
        
        # Si le paramètre est "oui"
        if fun:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("oui", width/2-100, height/1.3) # affichage relative aux dimensions de la fenêtre
        
        # Si le paramètre est "non"
        if not fun:
            fill(255, 255, 255) # le texte est blanc
        else: fill(0, 0, 0) # sinon  le texte est noir
        text("non", width/2+25 - 35, height/1.3) # affichage relative aux dimensions de la fenêtre
        
        # Détections des cliques sur les boutons
        if mousePressed and mouseX >= width/2-100 - 40 and mouseX <= width/2-100 - 40 + 40*2 and mouseY >= height/1.3 - 40 and mouseY <= height/1.3 - 40 + 45: # bouton "oui"
            self.jeu_options["fun"] = True # Activation du mode fun
        elif mousePressed and mouseX >= width/2+25 - 75 and mouseX <= width/2+25 - 75 +  40*3.75 and mouseY >=height/1.3 - 40 and mouseY <= height/1.3 - 40 + 45: # bouton "non"
            self.jeu_options["fun"] = False # Désactivation du mode fun
        
      ### Bouton "Jouer"
        # zone de clique
        fill(200, 100, 0) # couleur orange
        rect(width/2 - 60*2.5, height - height/7, 60*5, 60, 20) # affichage relative aux dimensions de la fenêtre
        # texte
        fill(255,255,255) # couleur blanche
        textSize(60) # taille du texte
        translate(mouseX, mouseY) # positions sur le curseur de la souris
        rotate(math.radians(self.jouer_angle)) # tourne le texte
        text("Jouer", 0, 0) # affiche le texte
        # mise à jour de l'angle
        self.jouer_angle += 1
        if self.jouer_angle == 360:
            self.jouer_angle = 0
            
    def vitesse_niveau(self):
        """
        Donne le paramètre de vitesse sous forme de chaine de caractère:
        | "lent", "normal" et "rapide"
        
        renvoie une chaine de caractère correspondant au paramètre de vitesse
        """
        if self.jeu_options["vitesse"] == 0.1: # Vitesse par défaut
            return "normal"
        elif self.jeu_options["vitesse"] > 0.1: # Vitesse plus lente 
            return "lent"
        else: # Vitesse plus rapide 
            return "rapide"
    
    def vie(self):
        """
        Donne le paramètre du nombre de vies
        
        renvoie un entier correspondant au nombre de vies
        """
        return self.jeu_options["vie"]
    
    def obstacle(self):
        """
        Donne le paramètre de l'activation des obstacles
        
        renvoie True si le paramètre est activé, False sinon
        """
        return self.jeu_options["obstacle"]
        
    def score_x4(self):
        """
        Donne le paramètre de l'activation du multiplicateur de score
        
        renvoie True si le paramètre est activé, False sinon
        """
        return self.jeu_options["score_x4"]
    
    def fun(self):
        """
        Donne le paramètre de l'activation du mode fun
        
        renvoie True si le paramètre est activé, False sinon
        """
        return self.jeu_options["fun"]
        


class Plateau:
    """
    La classe Plateau permet de créer un plateau de jeu pour le snake, son positionnement
      et sa taille est adapté au dimensions fournis
    
    - Plateau(w, h, taille_carreau)
        w: int | La largeur de la fenêtre
        h: int | La hauteur de la fenêtre
        taille_carreau: int | Dimensions d'un carreau du plateau en pixel
    
    Attributs:
        taille_carreau: int | Dimensions d'un carreau du plateau en pixel
        dimensions: tuple[int, int] | Dimensions en unité du plateau
        centre_x: int | Centre le plateau au centre des dimensions fournis en x
        centre_y: int | Centre le plateau au centre des dimensions fournis en y
        obstacles_liste: list | La liste des obstacles présent sur le plateau
        
    Méthodes:
        - afficher(): affiche les différents éléments du plateau
        - get_free_position(): cherche les positions libres en unité sur le plateau
        - get_obstacles_position(): donne les positions en unité des obstacles sur le plateau
        - get_pos_of(): convertie une unité de positions en pixel
        - set_obstacle(nombre): ajoute un ou plusieurs obstacle au plateau
    """
    
    def __init__(self, w, h, taille_carreau):
        self.taille_carreau = taille_carreau # dimensions d'un carreau du plateau en pixel
        self.dimensions = (int(w//self.taille_carreau)-2, int(h//self.taille_carreau)-2) # dimensions en unité du plateau
        self.centre_x = w//2 - self.dimensions[0]*self.taille_carreau//2 # centre le plateau au centre des dimensions fournis en x
        self.centre_y = h//2  - self.dimensions[1]*self.taille_carreau//2 # centre le plateau au centre des dimensions fournis en y
        # La liste des obstacles présent sur le plateau
        self.obstacles_liste = []
    
    def afficher(self):
        """
        Affiche les différents éléments du plateau
        
        ne renvoie rien
        """
        # Affichage des carreaux
        for y in range(self.dimensions[1]):
            for x in range(self.dimensions[0]):
                fill(0,200,100) # couleur herbe fraîchement verte
                pos_x, pos_y = self.get_pos_of(x, y) # convertie les unités en pixel
                rect(pos_x , pos_y, self.taille_carreau, self.taille_carreau) # affiche le carreau
        # Affichage des obstacles
        for obst in self.obstacles_liste:
            obst.afficher()
                
    def get_pos_of(self, x, y):
        """
        Convertie une unité de positions en pixel
        
        renvoie un tuple des valeurs x et y convertie
        """
        pos_x = x*self.taille_carreau + self.centre_x
        pos_y = y*self.taille_carreau + self.centre_y
        return pos_x, pos_y
    
    def set_obstacle(self, nombre):
        """
        Ajoute un ou plusieurs obstacle au plateau
        
        Paramètre:
            nombre: int | Le nombre d'obstacle à rajouter
        
        ne renvoie rien
        """
        for i in range(nombre):
            self.obstacles_liste.append( Obstacle(self) )
    
    def get_obstacles_position(self):
        """
        Donne les positions en unité des obstacles sur le plateau
        
        renvoie une liste des attributs (positions) x et y des obstacles 
        """
        positions = []
        # Parcours de la liste d'obstacles
        for obst in self.obstacles_liste:
            positions.append(obst.get_pos())
        return positions
    
    def get_free_position(self):
        """
        Cherche les positions libres en unité sur le plateau
        
        renvoie une liste des attributs (positions) x et y des positions libres 
        """
        positions = []
        # On récupère la positions des obstacles
        obstacles_position = self.get_obstacles_position()
        # Parcours de chaque carreau
        for y in range(self.dimensions[1]):
            for x in range(self.dimensions[0]):
                # Si un obstacle n'occupe pas ce carreau
                if (x, y) not in obstacles_position:
                    positions.append( (x, y) ) # alors cette positions est libre
        return positions
    

class Jeu:
    """
    La classe Jeu gère le bon fonctionnement du jeu
    
    - Jeu(w, h, jeu_options)
        w: int | La largeur de la fenêtre
        h: int | La hauteur de la fenêtre
        jeu_options: dict | Les différents paramètres du jeu
    
    Attributs:
        compteur: int | Permet de réguler la vitesse du snake
        vitesse: int | Défini la vitesse du snake
        retour: bool | Indique si le jeu demande à retourner au menu principal
        is_fun: bool | Indique si le mode fun est activé
        angle: int | L'angle en degrés du plateau
        color_list: list | Une liste de couleur
        plateau: Plateau | Le plateau de jeu
        pomme: Pomme | La pomme du jeu
        grandir: int | Défini le nombre d'anneau que le snake doit grandir lorsqu'il mange une pomme
        snake: Snake | Le snake du jeu
        snake_vie: int | Le nombre de vie du snake
        (pour une question pratique le nombre de vie n'est pas stocké dans la classe Snake, car lorsque le snake perd une vie, il est supprimer et re-instancié)
    
    Methodes:
        - update(): met à jour les différents éléments du jeu
        - afficher(): affiche les différents éléments du jeu
        - retour_menu(): vérifie si le jeu demande de retourner au menu principal
        - faire_pause(seconde): permet de faire pause un nombre de seconde donné
    """
    
    def __init__(self, w, h, jeu_options):
        
        self.compteur = 0 # permet de réguler la vitesse du snake
        self.vitesse = jeu_options["vitesse"] * 30 # défini la vitesse du snake | 30 -> frequence d'affichage
        
        self.retour = False # indique si le jeu demande à retourner au menu principal
        
        self.grandir = 1 # défini le nombre d'anneau que le snake doit grandir lorsqu'il mange une pomme
        if jeu_options["score_x4"]:
            self.grandir = 4
        
        self.is_fun = jeu_options["fun"] # indique si le mode fun est activé
        if self.is_fun:
            # Redimentions du plateau
            w = int(w//1.6)
            h = int(h//1.6)
            
        self.angle = 0 # l'angle en degrés du plateau
        self.color_list = [
                          (255, 0, 255),
                          (255, 255, 0),
                          (0, 255, 255),
                          (175, 50, 255),
                          (255, 175, 50)
        ] # une liste de couleur
        
        # Le plateau de jeu
        self.plateau = Plateau(w, h, jeu_options["taille"])
        if jeu_options['obstacle']: # si les obstacles sont activés
            # Ajout d'obstacle ( 2% de l'espace libre )
            self.plateau.set_obstacle( int(0.02 * self.plateau.dimensions[0] * self.plateau.dimensions[1]) )
        # Le snake du jeu
        self.snake = Snake(0,0, self.plateau, (255,255,255))
        self.snake_vie = jeu_options["vie"] # le nombre de vie du snake
        # (pour une question pratique le nombre de vie n'est pas stocké dans la classe Snake, car lorsque le snake perd une vie, il est supprimer et re-instancié)
        
        # La pomme du jeu
        self.pomme = Pomme(self.plateau)
        
        self.faire_pause(0.5) # fait une pause 1/2 seconde avant le début du jeu
    
    
    def update(self):
        """
        Met à jour les différents éléments du jeu
        
        ne renvoie rien
        """
        # Si le snake est vivant
        if self.snake.est_vivant():
            self.compteur += 1
            
            # Gestion des entrées claviers
            if keyPressed:
                if key==CODED:
                    if keyCode == RIGHT and self.snake.direction != 'g': # Touche droite et direction du snake non opposé
                        # On change la direction
                        self.snake.changer_direction('d')
                    if keyCode == LEFT and self.snake.direction != 'd': # Touche gauche et direction du snake non opposé
                        # On change la direction
                        self.snake.changer_direction('g')
                    if keyCode == DOWN and self.snake.direction != 'h': # Touche bas et direction du snake non opposé
                        # On change la direction
                        self.snake.changer_direction('b')
                    if keyCode == UP and self.snake.direction != 'b': # Touche haut et direction du snake non opposé
                        # On change la direction
                        self.snake.changer_direction('h')
            
            # Régulation de la vitesse
            if self.compteur >= self.vitesse:
                self.compteur = 0
                
                # Si la barre espace est pressé
                if keyPressed:
                    if key == ' ':
                        # On ajoute un anneau au snake
                        self.snake.ajouter_anneau()
                
                # Le snake avance
                self.snake.avancer()
                
                # Si le snake est mort
                if not self.snake.est_vivant():
                    self.snake_vie -= 1 # il perd une vie
                    # Si il lui reste des vies supplémentaire
                    if self.snake_vie > 0:
                        # On récupère la longueur de sa queue
                        len_queue = self.snake.get_score()
                        # Création d'un nouveau snake
                        self.snake = Snake(0,0, self.plateau, (255,255,255))

                        self.faire_pause(1) # pause d'une seconde avant la reprise du jeu
                        # Ajout des anneaux au snake
                        self.snake.ajouter_anneau(len_queue)
                
                # Si le snake rencontre une pomme
                if self.snake.tete().get_pos() == self.pomme.get_pos():
                    # Nouvelle pomme !
                    self.pomme = Pomme(self.plateau)
                    self.snake.ajouter_anneau(self.grandir) # ajout d'un anneau au snake
    
    def afficher(self):
        """
        Affiche les différents éléments du jeu
        
        ne renvoie rien
        """
        # Si le mode fun est activé
        if self.is_fun:
            color_choosen = choice(self.color_list) # une couleur aléatoire parmis la liste de couleur
            # Application de la couleur à l'arrière plan
            background(color_choosen[0], color_choosen[1], color_choosen[2])
            # Le plateau ce place en positions "inverse" de la souris
            translate(width-mouseX, height-mouseY)
            rotate(math.radians(self.angle)) # fait tourné le plateau
            # mise à jour de l'angle
            self.angle += 1
            if self.angle >= 360:
                self.angle = 0
        
        self.plateau.afficher() # affichage du plateau
        self.snake.afficher() # affichage du snake
        self.pomme.afficher() # affichage de la pomme
        
        # Si le snake est mort
        if not self.snake.est_vivant():
            fill(100, 50, 255) # couleur violet
            textSize(60) # taille du texte
            textAlign(CENTER) # écriture en mode centré
            text("Perdu !", width/2, height/3) # affichage relative aux dimensions de la fenêtre
            text("Score:", width/2, height - height/3 - 30) # affichage relative aux dimensions de la fenêtre
            text(str(self.snake.get_score())+"\nCliquer pour rejouer", width/2, height - height/3+ 45*2 + 60/10) # affichage relative aux dimensions de la fenêtre
            self.retour = mousePressed # attente du clique de l'utilisateur pour demander le retour au menu
        
    
    def retour_menu(self):
        """
        Vérifie si le jeu demande de retourner au menu principal
        
        renvoie True si le jeu demande de retourner au menu principal, False sinon
        """
        return self.retour
            
    def faire_pause(self, seconde):
        """
        Permet de faire pause un nombre de seconde donné
        
        Paramètre:
            seconde: float | Un temps exprimé en seconde
            
        ne renvoie rien
        """
        self.compteur -= 30 * seconde # 30 -> fréquence d'affichage
