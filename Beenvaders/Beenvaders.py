import pygame, sys, threading
from display import Display
from level import Level
from save import Save
from shop import Shop


pygame.init()

screen=pygame.display.set_mode((1200, 900))
##Klasa zarzadzajaca dzialaniem gry
class Main:
    ##Konstruktor
    #@param screen ekran, na ktorym beda wyswietlane wszystkie grafiki i zmiany
    def __init__(self, screen):
        self.screen=screen
        self.FPS=pygame.time.Clock()
        self.actions={"choice":False,"choose_game":False,"choose_shop":False,"choose_reset":False,"choose_quit":False, "return": False, "up":False, "down":False, "win":False, "loss":False}
        self.save=Save()
        
    ##Metoda zbierajaca wydarzenia na ekranach startu i sklepu 
    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    self.actions["down"] = True
                if keys[pygame.K_UP]:
                    self.actions["up"] = True
                if keys[pygame.K_z]:
                    self.actions["choice"] =True
                if keys[pygame.K_ESCAPE]:
                    self.actions["return"]=True
    
    ##Metoda ekranu startu                
    def start(self):
        display=Display(self.screen)
        display.start_init_dis()
        display._load_cursor()
        
        selections={0:"Start",1:"Shop",2:"Reset",3:"Quit"}
        curr_select=0
        #kursor
        #waiting for selection
        while not self.actions["choice"]:
           
           display.start_dis()
           self.menu_events()
           curr_select=display._update_cursor(self.actions,curr_select,selections)
           pygame.display.update()
           self.FPS.tick(30)
           
        #selection made   
        if selections[curr_select]=="Start":
             self.actions["choose_game"]=True
              
        elif selections[curr_select]=="Shop":
                self.actions["choose_shop"]=True   
               
        elif selections[curr_select]=="Reset":
                self.actions["choose_reset"]=True
             
        elif selections[curr_select]=="Quit":
                self.actions["choose_quit"]=True 
        
        #reset to default
        self.actions["choice"]=False
        self.actions["return"]=False
        self.actions["loss"]=False
    
    ##Metoda ekranu sklepu
    def shop(self):
        shop=Shop(self.save.upgrades)
        display=Display(self.screen)
        display.load_shop_dis()
        selections={0:"Health",1:"Speed",2:"Points", 3:"Cowboy", 4:"Hawaii", 5:"Queen"}
        curr_select=0
        curr_score=self.save.get_score()
        
        while not self.actions["return"]:
            pygame.event.get()
            enough=shop.check_cost(curr_score, curr_select)
            display.shop_dis(curr_score, curr_select,shop.items, enough)
            self.menu_events()
            curr_select=display.update_shop_cursor(self.actions,curr_select,selections)
            if self.actions["choice"] and enough:
                curr_score=shop.purchase(curr_score, curr_select)
            self.actions["choice"]=False
            pygame.display.update()
        
        self.save.upgrades=shop.items
        self.save.score=curr_score
    
    ##Metoda ekranu instrukcji
    def instructions(self):
        display=Display(self.screen)
        skip=False
        while not skip:
            display.instruction_screen()
            self.menu_events()
            if self.actions["choice"]:
                skip=True
            elif self.actions["return"]:
                skip=True
            pygame.display.update()
            
        self.actions["choice"]=False
        self.actions["return"]=False
    
    ##Metoda watku zbierajacego wydarzenia na ekranie poziomu
    def event_thread(self, level):
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        level.player_move(attack=True, speed_upgrade=self.save.upgrades["Speed"])
                    if keys[pygame.K_ESCAPE]:
                        self.actions["return"]=True  

    ##Metoda ekranu poziomu
    def level(self, curr_level):
        display=Display(self.screen)
        level=Level(self.screen, self.save.get_score(), self.save.upgrades, curr_level)
        display.level_init_dis(curr_level)
        game_over=False
        leave_level=False
        
      
        #main loop
        while not game_over and not self.actions["return"]:
            display.level_dis(curr_level)
            other_events=threading.Thread(target=self.event_thread(level))
            other_events.start()
            level.player_move()
            level.update(self.save.upgrades["Point_up"])
            other_events.join()
            pygame.display.update()
            game_over=level.game_over
            self.actions["win"]=level.win
            self.actions["loss"]=level.loss
            self.FPS.tick(30)
        
        self.save._refresh_score(level.score) 
        
        #loss
        while not leave_level and self.actions["loss"]:
            pygame.time.wait(1)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        leave_level=True
                        self.actions["return"]=True
        #win
        while not leave_level and self.actions["win"]:
            pygame.time.wait(1)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        leave_level=True
                        self.actions["return"]=True
                    if event.key==pygame.K_SPACE:
                        leave_level=True
                        if curr_level==5:
                            self.actions["return"]=True
    
    ##Metoda resetujaca ulepszenia i punkty                          
    def reset(self):
        self.save._refresh_score(0)
        self.save._refresh_upgrades({"Health":0, "Speed": 0, "Point_up": 0, "Cowboy":False, "Cowboy_on":False, "Hawaii":False, "Hawaii_on":False, "Queen":False, "Queen_on":False})
    
    #Metoda petli gry
    def game_loop(self):
        self.start()
        curr_level=0
        while True:
            pygame.event.pump()
            #level
            if self.actions["choose_game"]==True:
                self.actions["choose_game"]=False
                self.instructions()
                
                curr_level=1
                for i in range (5):
                    self.level(curr_level)
                    curr_level+=1
                    if self.actions["loss"] or self.actions["return"]:
                        break
            #shop
            elif self.actions["choose_shop"]==True:
                self.actions["choose_shop"]=False
                self.shop()
            #reset
            elif self.actions["choose_reset"]==True:
                self.actions["choose_reset"]=False
                self.actions["return"]=True
                self.reset()
            #back to main menu
            elif self.actions["return"]==True:
                self.actions["return"]=False
                self.start()
            #exit
            elif self.actions["choose_quit"]==True:
                thread=threading.Thread(target=self.save.export_save())
                thread.start()
                thread.join()
                pygame.quit()
                sys.exit()
        

play = Main(screen)
play.game_loop()

