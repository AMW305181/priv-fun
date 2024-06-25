import pygame
from pathlib import Path

##Klasa reprezentujaca pociski wystrzeliwane przez gracza i przeciwnikow
class Bullet(pygame.sprite.Sprite):
    ##Konstruktor
    #@param pos tuple ze zmiennymi opisujacymi startowa pozycje pocisku
    #@param speed_upgrade informacja o ewentualnym przyspieszeniu szybkosci pocisku gracza
    def __init__(self, pos,side, speed_upgrade=0):
        super().__init__()
        self.x=pos[0]
        self.y=pos[1]
        img_path=Path.cwd()
        img_path=Path.joinpath(img_path,"assets","sprites","pocisk.png")
        self.image=pygame.image.load(img_path)
        
        if side =="enemy":
             self.speed=-10
             self.image=pygame.transform.flip(self.image,False, True)
             self.rect=self.image.get_rect(topleft=pos)
             self.mask=pygame.mask.from_surface(self.image)
        elif side=="player":
            self.speed=10+speed_upgrade*5
            self.rect=self.image.get_rect(topleft=pos)
            self.mask=pygame.mask.from_surface(self.image)
        
    ##Metoda odpowiadajaca za zmiane pozycji pocisku na osi y
    def _move(self):   
        self.rect.y-=self.speed
        
    ##Metoda aktualizujaca status pocisku   
    def update(self):
        self._move()
        self.rect=self.image.get_rect(topleft=(self.rect.x,self.rect.y))
        if self.rect.bottom<=0 or self.rect.top>=900:
            self.kill()
