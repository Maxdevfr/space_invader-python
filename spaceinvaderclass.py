import pyxel

class Ship:
    
    """Vaisseau principal"""
    def __init__(self,x,y):
        """
        Caracteristique du vaisseau.
        c'est un carre dans un premier temps'
    
        """
        self.x=x
        self.y=y
        self.taille=8
    
    
    def draw(self):
        """
        Affichage vaisseau 
    
        """
        decal=self.taille//2
        pyxel.rectb(self.x - decal, self.y - decal,self.taille,self.taille,7)
    def move (self,dx,dy):
        """
        deplacement du vaisseau 
        """
        self.x+=dx
        self.y+=dy
       
        if self.x < 0:
            self.x = 120
      
        if self.x>120:
            self.x=-1


def check_collision(missile, enemy):
    """
    Vérifie s'il y a collision entre un missile et un ennemi.
    
    True si colision, False sinon.
    """
    # Distance entre les centres des deux objets
    dist_x = abs(missile.x - enemy.x)
    dist_y = abs(missile.y - enemy.y)
    
    # Somme des demi-tailles
    demi_missile = missile.taille // 2
    demi_enemy = enemy.taille // 2
    
    # Il y a collision si les deux conditions sont vraies
    return dist_x < (demi_missile + demi_enemy) and dist_y < (demi_missile + demi_enemy)


class App:
    def __init__(self):
        pyxel.init(120, 200)
        self.ship = Ship(60, 180)
        self.enemies = []
        self.missiles = []
        self.score = 0
        self.game_over = False
        
        # Création des ennemis 
        espacement = 20
        for ligne in range(2):
            for colonne in range(6):
                x = 10 + colonne * espacement
                y = 10 + ligne * espacement
                self.enemies.append(Enemy(x, y))

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_RETURN):
                # Redémarrer le jeu
                self.__init__()
            return
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.ship.move(1, 0)

        if pyxel.btn(pyxel.KEY_LEFT):
            self.ship.move(-1, 0)

       
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.missiles.append(
                Missile(self.ship.x, self.ship.y - 6)
            )

     
        for missile in self.missiles[:]:
            missile.move()
            if missile.y < 0:
                self.missiles.remove(missile)

        for enemy in self.enemies:
            enemy.move(0.3)
            
            # Vérifier collision avec le vaisseau
            if check_collision(self.ship, enemy):
                self.game_over = True
            
            # Game over si ennemi descend trop bas
            if enemy.y > 200:
                self.game_over = True
        
        # Vérifier collisions missile-ennemi
        for missile in self.missiles[:]:
            for enemy in self.enemies[:]:
                if check_collision(missile, enemy):
                    # Enlever le missile et l'ennemi
                    if missile in self.missiles:
                        self.missiles.remove(missile)
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                    # Ajouter au score
                    self.score += 10
                    break

    def draw(self):
        pyxel.cls(0)
        self.ship.draw()
        for missile in self.missiles:
            missile.draw()
        for enemy in self.enemies:
            enemy.draw()
        
        # Afficher le score
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        
        # Afficher game over
        if self.game_over:
            pyxel.text(30, 90, "GAME OVER", 8)
            pyxel.text(15, 110, "Appuyer ENTREE", 7)


class Missile:
    def __init__(self, x, y, taille=2):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = -2  # vers le haut

    def move(self):
        self.y += self.vitesse

    def draw(self):
        decal = self.taille // 2
        pyxel.rect(self.x - decal, self.y - decal,
                   self.taille, self.taille, 8)



class Enemy:
    """Un seul ennemi"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taille = 9  # Taille du carré de l'ennemi
    
    def draw(self):
        """Affichage ennemi"""
        decal = self.taille // 2
        pyxel.rect(self.x - decal, self.y - decal, self.taille, self.taille, 9)
    
    def move(self, dy):
        """Déplacement ennemi"""
        self.y += dy

App()      
   


