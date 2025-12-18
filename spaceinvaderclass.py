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




class App:
    def __init__(self):
        pyxel.init(120, 200)
        self.ship = Ship(60, 180)

      
        self.missiles = []

        pyxel.run(self.update, self.draw)

    def update(self):
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

    def draw(self):
        pyxel.cls(0)
        self.ship.draw()
        for missile in self.missiles:
            missile.draw()



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


App()      

