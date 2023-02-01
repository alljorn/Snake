# coding: utf-8


class Anneau:
    """
    La classe Anneau permet de constitué le corps du snake
    
    - Anneau(pos_x, pos_y, plateau, couleur)
        pos_x: int | La position en unité sur le plateau en x
        pos_y: int | La position en unité sur le plateau en y
        plateau: Plateau | Le plateau sur laquelle appartient l'anneau
        couleur: tuple[int, int, int] | La couleur de l'anneau
    
    Attributs:
        cote: int | La taille des carreaux du plateau
        plateau: Plateau | Le plateau sur laquelle appartient l'anneau
        couleur: tuple[int, int, int] | La couleur de l'anneau
        x: int | La position en unité sur le plateau en x
        y: int | La position en unité sur le plateau en y
    
    Méthodes:
        - get_pos(): donne la position de l'anneau
        - afficher(): affiche l'anneau
        - changer_couleur(couleur): permet de changer la couleur de l'anneau
    """
    
    def __init__(self, pos_x, pos_y, plateau, couleur):
        self.x = pos_x # la position en unité sur le plateau en x
        self.y = pos_y # la position en unité sur le plateau en y
        self.cote = plateau.taille_carreau # la taille des carreaux du plateau
        self.plateau = plateau # le plateau fournit
        self.couleur = couleur # la couleur définit
    
    def get_pos(self):
        """
        Donne la position de l'anneau
        
        renvoie un tuple des positions x et y
        """
        return self.x, self.y
    
    def afficher(self):
        """
        Affiche l'anneau
        
        ne renvoie rien
        """
        r, v, b = self.couleur # couleur rouge, vert, bleu
        fill(r, v, b) # définition de la couleur
        pos_x, pos_y = self.plateau.get_pos_of(self.x, self.y) # récupère la position en pixel de l'anneau
        rect(pos_x, pos_y, self.cote, self.cote) # affichage
    
    def changer_couleur(self, couleur):
        """
        Permet de changer la couleur de l'anneau
        
        Paramètre:
            couleur: tuple[int, int, int] | La couleur de l'anneau
        
        ne renvoie rien
        """
        self.couleur = couleur


class Snake:
    """
    La classe Snake permet de créer un snake, son seul but est de faire grandir sa queue en mangeant des pommes
    
    - Snake(x, y, plateau, couleur)
        x: int | La position en unité sur le plateau en x
        y: int | La position en unité sur le plateau en y
        plateau: Plateau | Le plateau sur laquelle appartient le snake
        couleur: tuple[int, int, int] | La couleur du snake
    
    Attributs:
        plateau: Plateau | Le plateau sur laquelle appartient le snake
        direction: str | Le caractère représentant la direction du snake ( 'd', 'g', 'b', 'h' )
        vivant: bool [ Le snake est vivant ou non
        couleur: tuple[int, int, int] | La couleur du snake
        list_anneau: list[Anneau] | La liste des anneaux qui constitue le corps du snake
        ajouter_anneau_compteur: int | Permet de savoir de combien le snake doit grandir
    
    Méthodes:
        - avancer(): fait avancer le snake dans la direction définit
        - tete(): donne l'anneau de tête du snake
        - afficher(): affiche le snake
        - changer_direction(direction): permet de changer la direction du snake
        - ajouter_anneau(nombre): permet d'ajouter au compteur d'ajout d'anneau un ou plusieurs anneaux
        - get_positions_corp(): donne la position de chaque anneau du corps du snake (hors tête)
        - collision(): vérifie si il y a une collision entre le snake et le bord du plateau ou de sa propre queue ou un obsatcle
        - est_vivant(): vérifie si le snake est vivant
        - get_score(): donne le score du joueur
    """
    
    def __init__(self, x, y, plateau, couleur):
        self.couleur = couleur # la couleur définit
        self.plateau = plateau # le plateau fournit
        self.list_anneau = [Anneau(x, y, plateau, couleur)] # la liste des anneaux qui constitue le corps du snake
        self.direction = 'd' # le caractère représentant la direction du snake ( 'd', 'g', 'b', 'h')
        self.ajouter_anneau_compteur = 0 # permet de savoir de combien le snake doit grandir
        self.vivant = True # le snake est vivant
        
    def avancer(self):
        """
        Fait avancer le snake dans la direction définit
        
        ne renvoie rien
        """
        x, y = self.tete().get_pos() # récupère la position de la tête du snake
        # Si le snake est en collision avec les bords du plateau ou un obsatcle
        if self.collision():
            # On change la couleur de la tête
            self.tete().changer_couleur( (200, 100, 0) ) # couleur marron
            self.vivant = False # Le snake est mort
        # Si tout va bien
        else:
            # Celon la direction
            if self.direction == 'd':
                self.list_anneau.insert(0, Anneau(x+1, y, self.plateau, self.couleur)) # Ajout d'un anneau qui devient la tête à droite de la tête actuel
            elif self.direction == 'g':
                self.list_anneau.insert(0, Anneau(x-1, y, self.plateau, self.couleur))# Ajout d'un anneau qui devient la tête à gauche de la tête actuel
            elif self.direction == 'b':
                self.list_anneau.insert(0, Anneau(x, y+1, self.plateau, self.couleur))# Ajout d'un anneau qui devient la tête en bas de la tête actuel
            elif self.direction == 'h':
                self.list_anneau.insert(0, Anneau(x, y-1, self.plateau, self.couleur))# Ajout d'un anneau qui devient la tête en haut de la tête actuel
            
            # Tant que le compteur d'anneau à rajouter est n'est pas nul on ne supprime pas le dernier anneau de son corps
            if self.ajouter_anneau_compteur > 0:
                self.ajouter_anneau_compteur -= 1
            else:
                self.list_anneau.pop(-1) # Supprime le dernier anneau du corps du snake
    
    def tete(self):
        """
        Donne l'anneau de tête du snake
        
        renvoie un anneau correspondant à la tête du snake
        """
        return self.list_anneau[0]
    
    def afficher(self):
        """
        Affiche le snake
        
        ne renvoie rien
        """
        # On affiche le snake du bout de sa queue à sa tête pour que le changement de couleur de la tête du snake soit visible lors d'une collision
        for anneau in reversed(self.list_anneau):
            anneau.afficher()
        # (note: si la tête du snake aurait été le dernier anneau de la liste on aurait pas eu besoin d'inverser la liste d'anneau)
    
    def changer_direction(self, direction):
        """
        Permet de changer la direction du snake
        
        Paramètre:
            direction: str | Le caractère représentant la direction du snake ( 'd', 'g', 'b', 'h' )
        
        ne renvoie rien
        """
        self.direction = direction
    
    def ajouter_anneau(self, nombre=1):
        """
        Permet d'ajouter au compteur d'ajout d'anneau un ou plusieurs anneaux
        
        Paramètre:
            nombre: int = 1 | Le nombre d'anneau à ajouter, 1 si non renseigné
        
        ne renvoie rien
        """
        self.ajouter_anneau_compteur += nombre
    
    def get_positions_corp(self):
        """
        Donne la position de chaque anneau du corps du snake (hors tête)
        
        renvoie une liste contenant la position de chaque anneau du corps du snake (hors tête)
        """
        pos = []
        # Pour chaque anneau du corps du snake (hors tête)
        for i in range(1, len(self.list_anneau)):
            pos.append(self.list_anneau[i].get_pos()) # Ajout de sa position à la liste
        return pos
    
    def collision(self):
        """
        Vérifie si il y a une collision entre le snake et le bord du plateau ou de sa propre queue ou un obsatcle
        
        renvoie True si il y a une collision, False sinon
        """
        x, y = self.tete().get_pos() # récupère la position de la tête du snake
        # Si collision avec le bord du plateau
        if x < 0 or y < 0 or x >= self.plateau.dimensions[0] or y >= self.plateau.dimensions[1]:
            return True
        # Si collision avec sa propre queue ou un obstacle
        elif (x, y) in self.get_positions_corp() or (x, y) in self.plateau.get_obstacles_position():
            return True
        else:
            return False
    
    def est_vivant(self):
        """
        Vérifie si le snake est vivant
        
        renvoie True si le snake est vivant, False sinon
        """
        return self.vivant
    
    def get_score(self):
        """
        Donne le score du joueur
        
        renvoie un entier positif correspondant au score du joueur
        """
        # Le score correspond au nombre de pomme mangé soit la longueur de la queue du snake
        return len(self.list_anneau) - 1
