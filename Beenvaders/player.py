import pygame
from bullet import Bullet
from pathlib import Path
##Klasa reprezentujaca gracza
class Player(pygame.sprite.Sprite):
    ##Konstruktor
    #@param pos startowa pozycja
    #@param health_upgrade posiadane ulepszenie punktow zycia
    #@param cowboy informacja czy kostium kowboja zostal zalozony
    #@param hawaii informacja czy kostium wakacyjny zostal zalozony    
    #@param queen informacja czy kostium krolowej zostal zalozony
    def __init__(self, pos, health_upgrade, cowboy, hawaii, queen):
        super().__init__()
        self.x=pos[0]
        self.y=pos[1]
        img_path=Path.cwd()
        if cowboy:
            img_path=Path.joinpath(img_path,"assets","sprites","bee_cowboy.png")
        elif hawaii:
            img_path=Path.joinpath(img_path,"assets","sprites","bee_hawaii.png")
        elif queen:
            img_path=Path.joinpath(img_path,"assets","sprites","bee_mainqueen.png")
        else:
            img_path=Path.joinpath(img_path,"assets","sprites","bee_main.png")
        self.image=pygame.image.load(img_path)
        self.rect=self.image.get_rect(topleft=pos)
        self.mask=pygame.mask.from_surface(self.image)
        #speed
        self.speed=20
        #lives
        self.lives=3+health_upgrade
        self.bullets=pygame.sprite.Group()
    
    ##Metoda zmieniajaca pozycje gracza
    #@param key przycisniety przycisk    
    def move(self, key):
        
        if(key[pygame.K_LEFT]):
            if self.rect.left>0:
                self.rect.x-=self.speed
                
        if(key[pygame.K_RIGHT]):
            if self.rect.right<1200:
                self.rect.x+=self.speed
                
    ##Metoda generujaca pocisk
    #@param speed_upgrade ulepszenie szybkosci pocisku gracza             
    def _shoot(self, speed_upgrade):
        current_pos=(self.rect.centerx-(30/2),self.rect.y)
        self.bullets.add(Bullet(current_pos,"player", speed_upgrade))
        
    ##Metoda aktualizujaca atrybut rectangle gracza    
    def update(self):
        self.rect=self.image.get_rect(topleft=(self.rect.x, self.rect.y))
