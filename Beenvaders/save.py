
import re
from pathlib import Path
##Klasa importujaca i eksportujaca plik zapisu, przechowuje i aktualizuje dane z zapisu, ktore przekazuje innym klasom
class Save():
    ##Konstruktor
    #@param path domyslna sciezka do pliku zapisu
    def __init__(self, path=Path.joinpath(Path.cwd(),"assets","save_file.txt")):
        
        with open(path, "r") as file:
            content=file.read()
            #saved score
            score_info=re.search("^score:\\s*\\d+", content)
            score_info=score_info.group()
            score_info=re.search("\\d+", score_info)
            score_info=score_info.group()
            self.score=int(score_info)
            #purchased items
            #health
            items_info=re.search("health\\s*\\d+", content)
            items_info=items_info.group()
            items_info=re.search("\\d+", items_info)
            items_info=items_info.group()
            health=int(items_info)
            #bullet speed
            items_info=re.search("bullet speed\\s*\\d+", content)
            items_info=items_info.group()
            items_info=re.search("\\d+", items_info)
            items_info=items_info.group()
            speed_upgrade=int(items_info)
            #point multiplier
            items_info=re.search("point multi\\s*\\d+", content)
            items_info=items_info.group()
            items_info=re.search("\\d+", items_info)
            items_info=items_info.group()
            point_upgrade=int(items_info)
            
            #cosmetics
            #cowboy
            items_info=re.search("cowboy\\s\\d\\son\\s\\d", content)
            items_info=items_info.group()
            items_info=re.findall("\\d", items_info)
            cowboy_purchased=bool(int(items_info[0]))
            cowboy_on=bool(int(items_info[1]))
            #hawaii
            items_info=re.search("hawaii\\s\\d\\son\\s\\d", content)
            items_info=items_info.group()
            items_info=re.findall("\\d", items_info)
            hawaii_purchased=bool(int(items_info[0]))
            hawaii_on=bool(int(items_info[1]))
            #queen
            items_info=re.search("queen\\s\\s\\d\\son\\s\\d", content)
            items_info=items_info.group()
            items_info=re.findall("\\d", items_info)
            queen_purchased=bool(int(items_info[0]))
            queen_on=bool(int(items_info[1]))
            self.upgrades={"Health":health, "Speed":speed_upgrade, "Point_up":point_upgrade, "Cowboy":cowboy_purchased, "Cowboy_on":cowboy_on, "Hawaii":hawaii_purchased, "Hawaii_on":hawaii_on, "Queen":queen_purchased, "Queen_on":queen_on}
            
    ##Metoda odswiezajaca laczna liczbe punktow gracza po wyjsciu ze sklepu lub poziomu    
    def _refresh_score(self, score):
        self.score=score
        
    ##Metoda zwracajaca przechowywana liczbe punktow 
    #@return laczna liczba punktow     
    def get_score(self):
        return self.score
    
    ##Metoda odswiezajaca informacje o ulepszeniach gracza po wyjsciu ze sklepu
    #@return slownik posiadanych ulepszen
    def _refresh_upgrades(self, upgrades):
        self.upgrades=upgrades
        
    ##Metoda eksportujaca plik zapisu 
    #@param path domyslna scieka do pliku  
    def export_save(self, path=Path.joinpath(Path.cwd(),"assets","save_file.txt")):
        with open(path, "w") as file:
            file.write(f"score: {self.score}\n")
            file.write("shop items:\n")
            file.write(f"\t\thealth {self.upgrades["Health"]}\n")
            file.write(f"\t\tbullet speed {self.upgrades["Speed"]}\n")
            file.write(f"\t\tpoint multi {self.upgrades["Point_up"]}\n")
            file.write(f"\t\tcowboy {int(self.upgrades["Cowboy"])} on {int(self.upgrades["Cowboy_on"])}\n")
            file.write(f"\t\thawaii {int(self.upgrades["Hawaii"])} on {int(self.upgrades["Hawaii_on"])}\n")
            file.write(f"\t\tqueen  {int(self.upgrades["Queen"])} on {int(self.upgrades["Queen_on"])}\n")





