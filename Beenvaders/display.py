import pygame
from pathlib import Path

pygame.font.init()
##Klasa nadzorujaca wyswietlanie elementow graficznych na ekranie
class Display:
    ##Konstruktor
    #@param screen ekran, na ktorym wyswietlane sa grafiki
    def __init__(self, screen):
        self.screen=screen
        self.score_font=pygame.font.SysFont("Segoe UI",80,True)
        self.text_color=pygame.Color(212,201,140)
        self.game_over_col=pygame.Color("red")
        self.start_font=pygame.font.SysFont("Segoe UI",60,True)
        self.start_text_col=pygame.Color(214,129,72)
        self.shop_font=pygame.font.SysFont("Segoe UI", 50, True)
        self.shop_desc_font=pygame.font.SysFont("Segoe UI", 30, True)
        self.shop_font_col=pygame.Color(242,242,242)

    ##Metoda ladujaca tlo i kursor ekranu startu 
    def start_init_dis(self):
        img_path=Path.joinpath(Path.cwd(), "assets", "backgrounds", "main_menu.png")
        self.main_image=pygame.image.load(img_path)
        self._load_cursor()
        
    ##Metoda wyswietlajaca ekran startu    
    def start_dis(self):
        self.screen.blit(self.main_image,(0,0))
        self._start_button_dis()
        
    ##Metoda generujaca tekst przyciskow na ekranie startu    
    def _start_button_dis(self):
        base_x=526
        start_text=self.start_font.render('START', True, self.start_text_col)
        self.screen.blit(start_text,(base_x,900-340))
        shop_text=self.start_font.render('SKLEP', True, self.start_text_col)
        self.screen.blit(shop_text,(base_x,900-270))
        reset_text=self.start_font.render('RESET',True, self.start_text_col)
        self.screen.blit(reset_text,(base_x,900-200))
        exit_text=self.start_font.render('WYJDZ', True, self.start_text_col)
        self.screen.blit(exit_text,(base_x,900-130))
    
    ##Metoda ladujaca grafike kursora oraz ustawiajaca jego startowa pozycje    
    def _load_cursor(self):
        img_path=Path.cwd()
        img_path=Path.joinpath(img_path, "assets", "sprites","cursor_main.png")
        self.cursor_image=pygame.image.load(img_path)
        self.cursor_basepos_y=900-307
        self.screen.blit(self.cursor_image,(500,self.cursor_basepos_y))
    
    ##Metoda aktualizujaca pozycje kursora
    #@param actions slownik zawierajacy m.in. informacje o kierunku, w ktorym ma sie przesunac kursor
    #@curr_select numer obecnie wybranego przycisku
    #@selections slownik dostepnych wyborow
    #@return curr_select    
    def _update_cursor(self, actions, curr_select, selections):
        if actions["down"]:
            curr_select = (curr_select + 1) % len(selections)
        elif actions["up"]:
            curr_select = (curr_select - 1) % len(selections)
        self.cursor_rect_y = self.cursor_basepos_y + (curr_select * 70)
        self.screen.blit(self.cursor_image,(500,self.cursor_rect_y))
        actions["down"]=False
        actions["up"]=False
        return curr_select
    
    ##Metoda wyswietlajaca ekran sklepu
    #@param score posiadane srodki
    #@param curr_select obecnie wybrane ulepszenie
    #@purchased slownik zakupionych ulepszen
    #@enough informacja, czy gracz posiada wystarczajace srodki do zakupu
    def shop_dis(self, score, curr_select, purchased, enough):
        
        self.screen.blit(self.shop_image,(0,0))
        
        #items
        health_upgrade_txt=self.shop_font.render('PUNKTY ZYCIA', True, self.shop_font_col)
        self.screen.blit(health_upgrade_txt,(50,90))
        j=0
        for i in range (purchased["Health"]):
          self.screen.blit(self.full_slot_image,(60+(45*i),155))
          j+=1
        for j in range (4):
            self.screen.blit(self.empty_slot_image,(60+(45*j),155))
        j=0   
        speed_upgrade_txt=self.shop_font.render('SZYBKOSC POCISKU', True, self.shop_font_col)
        self.screen.blit(speed_upgrade_txt,(50, 200))
        for i in range (purchased["Speed"]):
            self.screen.blit(self.full_slot_image,(60+(45*i),265))
            j+=1
        for j in range (4):
            self.screen.blit(self.empty_slot_image,(60+(45*j),265))
        j=0
        point_upgrade_txt=self.shop_font.render('BONUS DO PUNKTOW', True, self.shop_font_col)
        self.screen.blit(point_upgrade_txt, (50, 310))
        for i in range (purchased["Point_up"]):
            self.screen.blit(self.full_slot_image,(60+(45*i),375))
            j+=1
        for j in range (4):
          self.screen.blit(self.empty_slot_image,(60+(45*j),375))
          
        cowboy_txt=self.shop_font.render('KOWBOJKA', True, self.shop_font_col)
        self.screen.blit(cowboy_txt,(50,420))
        if purchased["Cowboy"]:
            self.screen.blit(self.full_slot_image,(60,485))
        else:
            self.screen.blit(self.empty_slot_image,(60,485))
        put_txt=self.shop_font.render('ZALOZ:', True, self.shop_font_col)
        self.screen.blit(put_txt,(120, 470))
        if purchased["Cowboy_on"]:
            self.screen.blit(self.full_slot_image,(300,485))
        else:
            self.screen.blit(self.empty_slot_image,(300,485))
            
        hawaii_txt=self.shop_font.render('WAKACYJNA', True, self.shop_font_col)
        self.screen.blit(hawaii_txt,(50,530))
        if purchased["Hawaii"]:
            self.screen.blit(self.full_slot_image,(60,595))
        else:
            self.screen.blit(self.empty_slot_image,(60,595))
        self.screen.blit(put_txt,(120, 580))
        if purchased["Hawaii_on"]:
            self.screen.blit(self.full_slot_image,(300,595))
        else:
            self.screen.blit(self.empty_slot_image,(300,595))
            
        queen_txt=self.shop_font.render('KROLEWSKA', True, self.shop_font_col)
        self.screen.blit(queen_txt,(50,640))
        if purchased["Queen"]:
            self.screen.blit(self.full_slot_image,(60,705))
        else:
            self.screen.blit(self.empty_slot_image,(60,705))
        self.screen.blit(put_txt,(120, 690))
        if purchased["Queen_on"]:
            self.screen.blit(self.full_slot_image,(300,705))
        else:
            self.screen.blit(self.empty_slot_image,(300,705))
        #item description
        not_enough_mess=self.shop_desc_font.render('NIEWYSTARCZAJACE SRODKI',True, self.shop_font_col)  
        max_upgrade_mess=self.shop_desc_font.render('MAKSYMALNIE ULEPSZONE', True, self.shop_font_col)
        match curr_select:
            case 0:
                health_desc1=self.shop_desc_font.render('ZWIEKSZA PUNKTY ZYCIA', True, self.shop_font_col)
                self.screen.blit(health_desc1, (730, 170))
                health_desc2=self.shop_desc_font.render('O 1 ZA KAZDY POZIOM',True, self.shop_font_col)
                self.screen.blit(health_desc2,(750, 200))
                health_cost=self.shop_desc_font.render('KOSZT: 100', True, self.shop_font_col)
                self.screen.blit(health_cost,(840,240))
                if not enough:
                    self.screen.blit(not_enough_mess,(710, 280))
                elif purchased["Health"]==4:
                    self.screen.blit(max_upgrade_mess,(720, 280))
                    
            case 1:
                speed_desc1=self.shop_desc_font.render('ZWIEKSZA SZYBKOSC', True, self.shop_font_col)
                self.screen.blit(speed_desc1,(770,170))
                speed_desc2=self.shop_desc_font.render('TWOICH POCISKOW', True, self.shop_font_col)
                self.screen.blit(speed_desc2,(780, 200))
                speed_cost=self.shop_desc_font.render('KOSZT: 200', True, self.shop_font_col)
                self.screen.blit(speed_cost,(840, 240))
                if not enough:
                    self.screen.blit(not_enough_mess,(710, 280))
                elif purchased["Speed"]==4:
                    self.screen.blit(max_upgrade_mess,(720, 280))
                    
            case 2:
                point_up_desc1=self.shop_desc_font.render('ZWIEKSZA ILOSC ZDOBYWANYCH', True, self.shop_font_col)
                self.screen.blit(point_up_desc1,(675, 170))
                point_up_desc2=self.shop_desc_font.render('PUNKTOW O 5 ZA KAZDY POZIOM', True, self.shop_font_col)
                self.screen.blit(point_up_desc2,(675, 200))
                point_cost=self.shop_desc_font.render('KOSZT: 300', True, self.shop_font_col)
                self.screen.blit(point_cost, (840, 240))
                if not enough:
                    self.screen.blit(not_enough_mess,(710, 280))
                elif purchased["Point_up"]==4:
                    self.screen.blit(max_upgrade_mess,(720, 280))
            case 3:
                cosmetic_desc=self.shop_desc_font.render('KOSTIUM',True, self.shop_font_col)
                self.screen.blit(cosmetic_desc,(850,130))
                self.screen.blit(self.cowboy_image,(850, 170))
                cowboy_cost=self.shop_desc_font.render('KOSZT: 700', True, self.shop_font_col)
                self.screen.blit(cowboy_cost,(840,270))
            case 4:
                cosmetic_desc=self.shop_desc_font.render('KOSTIUM',True, self.shop_font_col)
                self.screen.blit(cosmetic_desc,(850,130))
                self.screen.blit(self.hawaii_image,(850, 170))
                hawaii_cost=self.shop_desc_font.render('KOSZT: 2000', True, self.shop_font_col)
                self.screen.blit(hawaii_cost,(840,270))
            case 5:
                cosmetic_desc=self.shop_desc_font.render('KOSTIUM',True, self.shop_font_col)
                self.screen.blit(cosmetic_desc,(850,130))
                self.screen.blit(self.queen_image,(850, 170))
                queen_cost=self.shop_desc_font.render('KOSZT: 4000', True, self.shop_font_col)
                self.screen.blit(queen_cost,(840,270))
        #points
        points_avai_txt=self.shop_font.render('DOSTEPNE SRODKI:', True, self.shop_font_col)
        self.screen.blit(points_avai_txt, (690, 900-420))
        points_txt=self.shop_font.render(f'{score}',True, self.shop_font_col)
        self.screen.blit(points_txt,(875, 900-355))     

    ##Metoda ladujaca graficzne elementy sklepu
    def load_shop_dis(self):
        img_path=Path.joinpath(Path.cwd(), "assets", "backgrounds", "shop_menu.png")
        self.shop_image=pygame.image.load(img_path)
        img_path=Path.joinpath(Path.cwd(), "assets", "sprites", "empty_shop_slot.png")
        self.empty_slot_image=pygame.image.load(img_path)
        img_path=Path.joinpath(Path.cwd(), "assets", "sprites", "full_shop_slot.png")
        self.full_slot_image=pygame.image.load(img_path)
        img_path=Path.joinpath(Path.cwd(), "assets", "sprites", "cursor_shop.png")
        self.shop_cursor_image=pygame.image.load(img_path)
        self.shop_cursor_base_y=115
        img_path=Path.joinpath(Path.cwd(), "assets", "sprites", "bee_cowboy.png")
        self.cowboy_image=pygame.image.load(img_path)
        img_path=Path.joinpath(Path.cwd(), "assets", "sprites", "bee_hawaii.png")
        self.hawaii_image=pygame.image.load(img_path)
        img_path=Path.joinpath(Path.cwd(), "assets", "sprites", "bee_mainqueen.png")
        self.queen_image=pygame.image.load(img_path)
     
    ##Metoda aktualizujaca pozycje kursora na ekranie sklepu
    #@param actions slownik zawierajacy m.in. informacje o kierunku przesuniecia kursora
    #@param curr_select obecnie wybrane ulepszenie
    #@param selections slownik dostepnych wyborow
    #@return curr_select    
    def update_shop_cursor(self, actions, curr_select, selections):
        if actions["down"]:
            curr_select = (curr_select + 1) % len(selections)
        elif actions["up"]:
            curr_select = (curr_select - 1) % len(selections)
        self.cursor_rect_y = self.shop_cursor_base_y + (curr_select * 110)
        self.screen.blit(self.shop_cursor_image,(25,self.cursor_rect_y))
        actions["down"]=False
        actions["up"]=False
        return curr_select
     
   ##Metoda ladujaca tlo danego poziomu
   #@param curr_level numer obecnego poziomu 
    def level_init_dis(self, curr_level):
        match curr_level:
            case 1:
                img_path=Path.joinpath(Path.cwd(),"assets", "backgrounds","bee_tlo.png")
                self.level1_back=pygame.image.load(img_path)
            case 2:
                img_path=Path.joinpath(Path.cwd(),"assets", "backgrounds","bee_tlo2.png")
                self.level2_back=pygame.image.load(img_path)
            case 3:
                img_path=Path.joinpath(Path.cwd(),"assets", "backgrounds","bee_tlo3.png")
                self.level3_back=pygame.image.load(img_path)
            case 4:
                img_path=Path.joinpath(Path.cwd(),"assets", "backgrounds","bee_tlo4.png")
                self.level4_back=pygame.image.load(img_path)
            case 5:
                img_path=Path.joinpath(Path.cwd(),"assets", "backgrounds","bee_tlo5.png")
                self.level5_back=pygame.image.load(img_path)
    
    ##Metoda wyswietlajaca tlo danego poziomu
    #@param curr_level numer obecnego poziomu            
    def level_dis(self, curr_level):
        match curr_level:
            case 1:
              self.screen.blit(self.level1_back,(0,0))
            case 2:
                self.screen.blit(self.level2_back,(0,0))
            case 3:
                self.screen.blit(self.level3_back,(0,0))
            case 4:
                self.screen.blit(self.level4_back,(0,0))
            case 5:
                self.screen.blit(self.level5_back,(0,0))
    
    ##Metoda wyswietlajaca posiadane punktow zycia
    #@param curr_lives liczba posiadanych punktow zycia            
    def show_life(self, curr_lives):
        img_path=Path.cwd()
        img_path=Path.joinpath(img_path,"assets", "sprites","zycko.png")
        image=pygame.image.load(img_path)
        image_x=80/2
        if curr_lives!=0:
            for lives in range (curr_lives):
                self.screen.blit(image, (image_x,15))
                image_x+=85
    
    ##Metoda wyswietlajaca posiadane punkty
    #@param curr_score liczba posiadanych punktow 
    def show_score(self, curr_score):
        score_x=700
        curr_score=self.score_font.render(f'Punkty:{curr_score}',True,self.text_color)
        self.screen.blit(curr_score,(score_x, 0))
    
    ##Metoda wyswietlajaca wiadomosc o przegranej
    def game_over_mess(self):
        mess=self.score_font.render('KONIEC...', True, self.game_over_col)
        self.screen.blit(mess,(420,400))
    
    ##Metoda wyswietlajaca wiadomosc o wygranej
    #@param curr_level obecny poziom    
    def win_mess(self, curr_level):
        if curr_level!=5:
             mess1=self.score_font.render('ZWYCIESTWO', True, pygame.Color("red"))
             self.screen.blit(mess1,(360,240))
             mess2=self.score_font.render('NACISNIJ SPACJE,', True, pygame.Color("red"))
             self.screen.blit(mess2,(290,320))
             mess3=self.score_font.render('ABY PRZEJSC', True, pygame.Color("red"))
             self.screen.blit(mess3,(380, 400))
             mess4=self.score_font.render('DO KOLEJNEGO POZIOMU', True, pygame.Color("red"))
             self.screen.blit(mess4,(140, 480))
        else:
            mess1=self.score_font.render('ZWYCIESTWO', True, pygame.Color("red"))
            self.screen.blit(mess1,(360,320))
            mess2=self.score_font.render('KONIEC GRY', True, pygame.Color("red"))
            self.screen.blit(mess2,(380,400))
    
    ##Metoda wyswietlajaca ekran instrukcji
    def instruction_screen(self):
        self.screen.fill("black")
        mess1=self.score_font.render('INSTRUKCJA', True, pygame.Color("yellow"))
        self.screen.blit(mess1,(400, 240))
        mess2=self.score_font.render('PORUSZANIE SIE: STRZALKI', True, pygame.Color("yellow"))
        self.screen.blit(mess2,(100, 320))
        mess3=self.score_font.render('STRZELANIE: SPACJA', True, pygame.Color("yellow"))
        self.screen.blit(mess3,(150, 400))
        mess4=self.score_font.render('WYJSCIE DO MENU: ESC', True, pygame.Color("yellow"))
        self.screen.blit(mess4,(150, 480))
        mess5=self.score_font.render('NACISNIJ Z BY ROZPOCZAC', True, pygame.Color("yellow"))
        self.screen.blit(mess5,(120, 560))
                                     
        
        
