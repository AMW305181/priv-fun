import pygame
from player import Player
from bullet import Bullet
from display import Display
from enemy import Basic_drone, Wasp, Queen
##Klasa organizujaca gen3rowanie i dzialanie poziomow
class Level:
    ##Konstruktor
    #@param screen ekran, na ktorym wyswietlane sa zmiany
    #@param score zdobyte punkty
    #param curr_level poziom, ktory ma byc wygenerowany
    def __init__(self, screen, score, upgrades,curr_level):
        self.screen=screen
        self.player=pygame.sprite.GroupSingle()
        self.enemies=pygame.sprite.Group()
        self.display=Display(self.screen)
        self.game_over=False
        self.score=score
        self.curr_level=curr_level
        self.win=False
        self.loss=False
        self._generate_level(upgrades["Health"], upgrades["Cowboy_on"], upgrades["Hawaii_on"], upgrades["Queen_on"])
        
    ##Metoda generujaca grupe przeciwnikow    
    def generate_enemies(self):
        columns=4
        rows=5
        for y in range(rows):
            for x in range (columns):
                curr_x=101*x+5
                curr_y=75*y+5
                curr_pos=(curr_x,curr_y)
                match self.curr_level:
                    case 1:
                        self.enemies.add(Basic_drone(curr_pos))
                    case 2:
                        if y<2:
                            self.enemies.add(Wasp(curr_pos))
                        else:
                            self.enemies.add(Basic_drone(curr_pos))
                    case 3:
                        if y==0:
                            self.enemies.add(Queen(curr_pos))
                        elif y<3:
                            self.enemies.add(Wasp(curr_pos))
                        else:
                            self.enemies.add(Basic_drone(curr_pos))
                    case 4:
                        if y==0:
                            self.enemies.add(Queen(curr_pos))
                        elif y<4:
                            self.enemies.add(Wasp(curr_pos))
                        else:
                            self.enemies.add(Basic_drone(curr_pos))
                    case 5:
                        if y<2:
                            self.enemies.add(Queen(curr_pos))
                        else:
                            self.enemies.add(Wasp(curr_pos))
                            
    ##Metoda generujaca gracza oraz przeciwnikow
    #@param health_upgrade posiadane ulepszenie liczby punktow zycia przez gracza
    #@param cowboy informacja czy kostium kowboja zostal zalozony
    #@param hawaii informacja czy kostium wakacyjny zostal zalozony    
    #@param queen informacja czy kostium krolowej zostal zalozony                    
    def _generate_level(self, health_upgrade, cowboy, hawaii, queen):
        player_x=1200/2
        player_y=900-120
        player_cntr_size=150/2
        player_pos=(player_x-player_cntr_size, player_y)
        self.player.add(Player(player_pos, health_upgrade, cowboy, hawaii, queen))
        self.generate_enemies()
        self.enemy_dir="right"
        
    ##Metoda odpowiadajaca za ruch awatara gracza
    #@param attack informacja, czy zostal wcisniety przycisk strzalu
    #@param speed_upgrade ulepszenie szybkosci pocisku gracza    
    def player_move(self, attack=False, speed_upgrade=0):
        keys=pygame.key.get_pressed()
        if not self.game_over:
            self.player.sprite.move(keys)
        
       # if keys[pygame.K_SPACE] and not self.game_over:
        if attack==True and not self.game_over:    
            self.player.sprite._shoot(speed_upgrade)
    ##Metoda kontrolujaca ruch grupy przeciwnikow
    def _enemy_move(self):
        move_down=False
        for enemy in self.enemies.sprites():
            if self.enemy_dir=="right" and enemy.rect.right<1200 or self.enemy_dir=="left" and enemy.rect.left>0:
                move_down=False
            else:
                move_down=True
                if self.enemy_dir=="right":
                    self.enemy_dir="left"
                else:
                    self.enemy_dir="right" 
                break
        for enemy in self.enemies.sprites():
            if not move_down:
                enemy.move(self.enemy_dir)
            else:
                enemy.move("down")
                
    ##Metoda generujaca na ekranie liczbe punktow zycia gracza i laczna liczbe zdobytych punktow 
    def generate_additionals(self):
        self.display.show_life(self.player.sprite.lives)
        self.display.show_score(self.score)
     
    ##Metoda kontrolujaca wystrzelenie pocisku przez przeciwnikow    
    def _enemy_shoot(self):
        for enemy in self.enemies.sprites():
            if(1200-enemy.rect.x)//(101+5)==(1200-self.player.sprite.rect.x)//150:
                enemy._shoot()
                break
     
    ##Metoda sprawdzajaca czy zostaly spelnione warunki konca poziomu        
    def _end_check(self):
        #loss
        if self.player.sprite.lives <=0:
            self.game_over=True
            self.loss=True
            self.display.game_over_mess()
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom>=900-100:
                self.game_over=True
                self.loss=True
                self.display.game_over_mess()
                break
        #win    
        if len(self.enemies)==0:
            self.game_over=True
            self.win=True
            self.display.win_mess(self.curr_level)
            
    ##Metoda kontrolujaca kolizje i jej konsekwencje 
    #@param point_upgrade dodatkowe punkty, ktore moze zdobyc gracz   
    def _collision_detect(self, point_upgrade):
        player_attack_hit=pygame.sprite.groupcollide(self.enemies, self.player.sprite.bullets, False, True)
        if player_attack_hit:
            self.score+=10+point_upgrade*5
            for enemy in player_attack_hit:
                enemy.lives-=1
                if enemy.lives==0:
                    self.enemies.remove(enemy)
        
        for enemy in self.enemies.sprites():
            enemy_attack_hit=pygame.sprite.groupcollide(enemy.bullets, self.player, True,False)
            if enemy_attack_hit:
                self.player.sprite.lives-=1
                break
            
            enemy_player_hit=pygame.sprite.groupcollide(self.enemies,self.player, True, False)
            if enemy_player_hit:
                self.player.sprite.lives-=1
                
    ##Metoda aktualizujaca stan poziomu 
    #@param point_upgrade dodatkowe punkty, ktore moze zdobyc gracz          
    def update(self, point_upgrade):
        self._collision_detect(point_upgrade)
        self._enemy_move()
        self._enemy_shoot()
        
        self.player.sprite.bullets.update()
        self.player.sprite.bullets.draw(self.screen)
        [enemy.bullets.update() for enemy in self.enemies.sprites()]
        [enemy.bullets.draw(self.screen) for enemy in self.enemies.sprites()]
        
        self.player.update()
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        self.generate_additionals()
        self._end_check()
     
