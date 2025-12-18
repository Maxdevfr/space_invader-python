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
        """
        Init fenetre + elements
        """
        pyxel.init(120,200)
        self.ship = Ship(60,180)
        pyxel.run(self.update,self.draw)
        self.Missile=Missile(60,180)
        self.Missile=[]
    def update(self):
        """
        Mise a jour des positions et des etats
        Pas d'affichage ici
        """
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.ship.move(1,0)
          
        if pyxel.btn(pyxel.KEY_LEFT):
            self.ship.move(-1,0)
        
        if pyxel.btn(pyxel.KEY_SPACE):
            self.Missile.move(0,1)
            
    def draw(self):
        """
        on affiche les elements
        """
        pyxel.cls(0)
        self.ship.draw()
        
        
class Missile:
    
    def __init__(self,x,y,taille=2):
        """
        Caracteristique du vaisseau.
        c'est un carre dans un premier temps'
        
        """
        self.x=x
        self.y=y
        self.taille=taille
        
        self.Missile=[]
    def draw(self):
        """
  
    
        """
        decal=self.taille//2
        pyxel.rectb(self.x - decal, self.y - decal,self.taille,self.taille,7)
    def move (self,dy):
        """
       
        """
        self.x+=x
        self.y+=dy
       

App()      
