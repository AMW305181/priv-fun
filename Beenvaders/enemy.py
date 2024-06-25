import pygame
from pathlib import Path
from bullet import Bullet
##Klasa rodzica dla poszczegolnych klas wrogow
class Enemy(pygame.sprite.Sprite):
    ##Metoda zmieniajaca pozycje wroga
    #@param direction strona, w ktora przeciwnik ma sie poruszyc
    def move(self,direction):
        if direction=="left":
            self.rect.x-=self.speed
        elif direction=="right":
            self.rect.x+=self.speed
        elif direction=="down":
            self.rect.y+=self.speed+10
            
    ##Metoda genrujaca pocisk wroga        
    def _shoot(self):
        current_pos=(self.rect.centerx-15, self.rect.centery)
        self.bullets.add(Bullet(current_pos, "enemy"))
    ##Metoda aktualizujaca atrybut rectangle wroga    
    def update(self):
        self.rect=self.image.get_rect(topleft=(self.rect.x,self.rect.y))

##Klasa przeciwnika truten        
class Basic_drone(Enemy):
    ##Konstruktor
    #@param pos startowa pozycja
    def __init__(self, pos):
        super().__init__()
        self.x=pos[0]
        self.y=pos[1]
        img_path=Path.cwd()
        img_path=Path.joinpath(img_path, "assets","sprites","bee_basic_drone.png")
        self.image=pygame.image.load(img_path)
        self.image=pygame.transform.scale(self.image,(101,75))
        self.rect=self.image.get_rect(topleft=pos)
        self.mask=pygame.mask.from_surface(self.image)
        self.speed=5
        self.lives=1
        self.bullets=pygame.sprite.GroupSingle()

##Klasa przeciwnika osa   
class Wasp(Enemy):
    ##Konstruktor
    #@param pos startowa pozycja
    def __init__(self, pos):
        super().__init__()
        self.x=pos[0]
        self.y=pos[1]
        img_path=Path.cwd()
        img_path=Path.joinpath(img_path, "assets","sprites","bee_wasp.png")
        self.image=pygame.image.load(img_path)
        self.image=pygame.transform.scale(self.image,(101,75))
        self.rect=self.image.get_rect(topleft=pos)
        self.mask=pygame.mask.from_surface(self.image)
        self.speed=5
        self.lives=2
        self.bullets=pygame.sprite.GroupSingle()
##Klasa przeciwnika krolowa        
class Queen(Enemy):
    ##Konstruktor
    #@param pos startowa pozycja
    def __init__(self, pos):
        super().__init__()
        self.x=pos[0]
        self.y=pos[1]
        img_path=Path.cwd()
        img_path=Path.joinpath(img_path,"assets","sprites","bee_queen.png")
        self.image=pygame.image.load(img_path)
        self.image=pygame.transform.scale(self.image,(101,75))
        self.rect=self.image.get_rect(topleft=pos)
        self.mask=pygame.mask.from_surface(self.image)
        self.speed=5
        self.lives=3
        self.bullets=pygame.sprite.GroupSingle()
        
