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
        self.taille=16
    
    
    def draw(self):
        """
        Affichage vaisseau 
    
        """
        decal=self.taille//2
        pyxel.blt(self.x - decal, self.y - decal, 1, 0, 0, 16, 16)
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


def collision(missile, enemy):
    """
    Collision
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
        self.vague_num = 0  # Numéro de la vague
        self.enemy_speed = 0.3  # Vitesse initiale
        
        pyxel.load("ressources.pyxres")
        
        # Créer la première vague
        self.vague()

        pyxel.run(self.update, self.draw)

    def vague(self):
        """Crée une nouvelle vague d'ennemis"""
        self.enemies = []
        espacement = 20
        for ligne in range(2):
            for colonne in range(6):
                x = 10 + colonne * espacement
                y = 10 + ligne * espacement
                self.enemies.append(Enemy(x, y))
        # Augmenter la vitesse de la vague
        self.enemy_speed += 0.1
        self.vague_num += 1
   
    def update(self):
        if not self.game_over:
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
            enemy.move(self.enemy_speed)
            
            # Vérifier collision avec le vaisseau
            if collision(self.ship, enemy):
                self.game_over = True
            
            # Game over si ennemi descend trop bas
            if enemy.y > 200:
                self.game_over = True
        
        # Vérifier collisions missile-ennemi
        for missile in self.missiles[:]:
            for enemy in self.enemies[:]:
                if collision(missile, enemy):
                    # Enlever le missile et l'ennemi
                    if missile in self.missiles:
                        self.missiles.remove(missile)
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                        # son de collision
                        pyxel.play(0, 0)
                       
                    # Ajouter au score
                    self.score += 10
                    break
        
        # Vérifier si tous les ennemis sont morts pour créer une nouvelle vague
        if len(self.enemies) == 0:
            self.vague()

    def draw(self):
        pyxel.cls(0)
        self.ship.draw()
        for missile in self.missiles:
            missile.draw()
        for enemy in self.enemies:
            enemy.draw()
        
        # Afficher le score
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.text(5, 15, f"Vague: {self.vague_num}", 7)
        
        # Afficher game over
        if self.game_over:
            pyxel.text(40, 90, "GAME OVER", 8)


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
        self.taille = 16  # Taille du carré de l'ennemi
    
    def draw(self):
        """Affichage ennemi"""
        decal = self.taille // 2
        pyxel.blt(self.x - decal, self.y - decal, 0, 0, 0, 16, 16)
    
    def move(self, dy):
        """Déplacement ennemi"""
        self.y += dy

App()
