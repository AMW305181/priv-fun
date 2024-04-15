

path = "lorem.txt"
#robi sobie slowniczek
with open(path,"r") as file:
    content =file.read()
    histogram = dict()
    for i in range(len(content)):
        histogram[content[i]]=0
    for i in range(len(content)):
        histogram[content[i]]+=1
    
keys =str(histogram.keys())
#zakomentowany blok to po prostu moje sprawdzenie kluczy i tego, czy faktycznie 107 w ascii to 'k'
'''print(keys)
print("\n")
print(chr(107))'''

#petla na tworzenie pliku z histogramem - klucz szukany przez konwersje z ascii na znak
path2 = "histogram.txt"
with open(path2, "w") as file:
    for i in range(26):#wielkie litery
        if(keys.find(chr(i+65))!=-1):
            file.write(chr(i+65))
            file.write(": ")
            file.write(str(histogram[chr(i+65)]))
            file.write("\n")
        else:
            file.write(chr(i+65))
            file.write(": 0\n")
    for i in range(26):#male litery
        if(keys.find(chr(i+97))!=-1):#blad robi sie tutaj przy malym 'k' - i 10, wchodzi w warunek, mimo, ze nie powinien
            file.write(chr(i+97))
            file.write(": ")
            file.write(str(histogram[chr(i+97)]))
            file.write("\n")
        else:
            file.write(chr(i+97))
            file.write(": 0\n")
        
        
