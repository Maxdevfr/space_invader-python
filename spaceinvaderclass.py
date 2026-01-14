import pyxel
import random


class Ship:
    
    """Vaisseau principal"""
    
    def __init__(self,x,y):
 
        self.x=x
        self.y=y
        self.taille=16
    
    
    def draw(self):
 
        decal=self.taille//2
        pyxel.blt(self.x - decal, self.y - decal, 1, 0, 0, 16, 16)


    def move (self,dx,dy):
        
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
   
    dist_x = abs(missile.x - enemy.x)
    dist_y = abs(missile.y - enemy.y) 
    
  
    demi_missile = missile.taille // 2
    demi_enemy = enemy.taille // 2
    
    
    return dist_x < (demi_missile + demi_enemy) and dist_y < (demi_missile + demi_enemy)


class App:
    def __init__(self):
        pyxel.init(120, 200)
        self.ship = Ship(60, 180)
        self.enemies = []
        self.missiles = []
        self.enemy_missiles = []  
        self.score = 0
        self.game_over = False
        self.vague_num = 0 
        self.enemy_speed = 0.3  
        pyxel.load("ressources.pyxres")
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

            
            for enemy in self.enemies:
                if random.random() < 0.01:  
                    self.enemy_missiles.append(
                        EnemyMissile(enemy.x, enemy.y + 8)
                    )
     
            for missile in self.missiles[:]:
                missile.move()
                if missile.y < 0:
                    self.missiles.remove(missile)

           
            for enemy_missile in self.enemy_missiles[:]:
                enemy_missile.move()
                if enemy_missile.y > 200:
                    self.enemy_missiles.remove(enemy_missile)
                
                
                if collision(self.ship, enemy_missile):
                    self.game_over = True
                    pyxel.play(0, 2)  
                    
                    if enemy_missile in self.enemy_missiles:
                        self.enemy_missiles.remove(enemy_missile)

            for enemy in self.enemies:
                enemy.move(self.enemy_speed)
                
                
                if collision(self.ship, enemy):
                    self.game_over = True
                    pyxel.play(0, 2) 
                
                
                if enemy.y > 200:
                    self.game_over = True
            
            
            for missile in self.missiles[:]:
                for enemy in self.enemies[:]:
                    if collision(missile, enemy):
                        
                        if missile in self.missiles:
                            self.missiles.remove(missile)
                        if enemy in self.enemies:
                            self.enemies.remove(enemy)
                           
                        pyxel.play(0, 0)  
                        self.score += 10
                        break
            
           
            if len(self.enemies) == 0:
                self.vague()

    def draw(self):
        pyxel.cls(0)
        
       
        if self.game_over:
            pyxel.text(40, 90, "GAME OVER", 8)
            pyxel.text(40, 110, f"Score: {self.score}", 20)
            pyxel.text(40, 130, f"Vague: {self.vague_num}", 20)
            return
        
       
        self.ship.draw()
        
        for missile in self.missiles:
            missile.draw()
        for enemy_missile in self.enemy_missiles:
            enemy_missile.draw()
        for enemy in self.enemies:
            enemy.draw()
        
       
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.text(5, 15, f"Vague: {self.vague_num}", 7)


class Missile:
    def __init__(self, x, y, taille=2):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = -2 

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
        self.taille = 16  
    
    def draw(self):
        """Affichage ennemi"""
        decal = self.taille // 2
        pyxel.blt(self.x - decal, self.y - decal, 0, 0, 0, 16, 16)
    
    def move(self, dy):
        """Déplacement ennemi"""
        self.y += dy


class EnemyMissile:
    """Missile tiré par un ennemi"""
    def __init__(self, x, y, taille=2):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = 1 

    def move(self):
        self.y += self.vitesse

    def draw(self):
        decal = self.taille // 2
        pyxel.rect(self.x - decal, self.y - decal, self.taille, self.taille, 10)

App()




