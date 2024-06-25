from display import Display
##Klasa odpowiadajaca za interakcje ze sklepem
class Shop():
    ##Konstruktor
    #@param purchased slownik posiadanych ulepszen
    def __init__(self, purchased):
        self.items=purchased
        self.health_cost=100
        self.speed_cost=200
        self.point_up_cost=300
        self.cowboy_cost=700
        self.hawaii_cost=2000
        self.queen_cost=4000
    
    ##Metoda sprawdzajaca, czy gracza stac na dane ulepszenie
    #@param curr_score posiadane srodki
    #@param curr_selection wybrane ulepszenie 
    #@return informacja, czy posiadane srodki sa wystarczajace na zakup ulepszenia   
    def check_cost(self, curr_score, curr_selection):
        enough=False
        match curr_selection:
            case 0:
                 if curr_score>=self.health_cost:
                     enough=True
            case 1:
                 if curr_score>=self.speed_cost:
                     enough=True
            case 2:
                 if curr_score>=self.point_up_cost:
                     enough=True
            case 3:
                if curr_score>=self.cowboy_cost:
                    enough=True
                elif self.items["Cowboy"]==True:
                    enough=True
            case 4:
                if curr_score>=self.hawaii_cost:
                    enough=True
                elif self.items["Hawaii"]==True:
                    enough=True
            case 5:
                if curr_score>=self.queen_cost:
                    enough=True
                elif self.items["Queen"]==True:   
                    enough=True

        return enough
    
    ##Metoda odpowiadajaca za zakup ulepszenia lub zalozenie kostiumu
    #@param curr_score posiadane srodki
    #@param curr_selection wybrane ulepszenie
    #@return curr_score
    def purchase(self,curr_score, curr_selection):
        
        match curr_selection:
            case 0:
                if self.items["Health"]<4:
                   self.items["Health"]+=1
                   return curr_score-self.health_cost
            case 1:
                if self.items["Speed"]<4:
                   self.items["Speed"]+=5  
                   return curr_score-self.speeed_cost
            case 2:
                if self.items["Point_up"]<4:
                   self.items["Point_up"]+=1
                   return curr_score-self.point_up_cost
            case 3:
                if self.items["Cowboy"]==False:
                    self.items["Cowboy"]=True
                    return curr_score-self.cowboy_cost
                elif self.items["Cowboy_on"]==False:
                    self.items["Cowboy_on"]=True
                    self.items["Hawaii_on"]=False
                    self.items["Queen_on"]=False
            case 4:
                if self.items["Hawaii"]==False:
                    self.items["Hawaii"]=True
                    return curr_score-self.hawaii_cost
                elif self.items["Hawaii_on"]==False:
                    self.items["Cowboy_on"]=False
                    self.items["Hawaii_on"]=True
                    self.items["Queen_on"]=False
            case 5:
                if self.items["Queen"]==False:
                    self.items["Queen"]=True
                    return curr_score-self.hawaii_cost
                elif self.items["Queen_on"]==False:
                    self.items["Cowboy_on"]=False
                    self.items["Hawaii_on"]=False
                    self.items["Queen_on"]=True
        return curr_score
    

