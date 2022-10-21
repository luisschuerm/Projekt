from GPIO import LED,Sensor,LCD, Luefter
import time
Gruen = LED("gruen")
Gruen.aus()
Rot=LED("rot")
Rot.aus()
Gelb = LED("gelb")
Gelb.aus()
Fan = Luefter()
Sensor = Sensor("28-00000a2aa46c")
L=LCD()
def Lichtorgel():
    while True:
        Rot.an()
        time.sleep(2)
        Rot.aus()
        Gelb.an()
        time.sleep(2)
        Gelb.aus()
        Gruen.an()
        time.sleep(2)
        Gruen.aus()


def Temp_Farbe():
    while (True):
        time.sleep(1)
        Wert = float(Sensor.lesen())
        L.schreiben("    "+str(Wert)+" C    ",2)
        print(Wert)
        
        if Wert <20:
            L.loeschen()
            L.schreiben("kalt",1)
            L.schreiben("    "+str(Wert)+" C    ",2)

            Fan.aus()
            Rot.aus()
            Gelb.aus()
            Gruen.an()
        
        elif Wert >=20 and Wert <30:
            L.loeschen()
            L.schreiben("Mittel",1)
            L.schreiben("    "+str(Wert)+" C    ",2)

            Fan.aus()

            Rot.aus()
            Gelb.an()
        elif Wert >=30:
            L.loeschen()
            L.schreiben("Heiss",1)
            L.schreiben("    "+str(Wert)+" C    ",2)

            Fan.an()
            Rot.an()
            Gelb.aus()
            Gruen.aus()
def Farb_Eingabe():
    while (True):
        Farbe= input("Farbe eingeben: ")
    
        if Farbe =="Gruen" or Farbe=="Grün":
            Rot.aus()
            Gelb.aus()
            Gruen.an()
        
        elif Farbe=="Gelb" :
            Gruen.aus()

            Rot.aus()
            Gelb.an()
        elif Farbe=="Rot":
           
            Rot.an()
            Gelb.aus()
            Gruen.aus()
        elif Farbe=="exit":
            print("tschau")
            break
def Eingabe_Temperatur():
    min = input("Min eingeben: ")
    max = input("Max eingeben: ")
    
    while True:
        Wert = float(Sensor.lesen())
        L.schreiben("    "+str(Wert)+" C    ",2)
        if Wert <min:
            L.schreiben("kalt")
            Fan.aus()
            Rot.aus()
            Gelb.aus()
            Gruen.an()
        
        elif Wert >min and Wert <max:
            L.schreiben("Mittel")
            Fan.aus()

            Rot.aus()
            Gelb.an()
        elif Wert >=max:
            L.schreiben("Heiß")
            Fan.an()
            Rot.an()
            Gelb.aus()
            Gruen.aus()

#Lichtorgel()
#Eingabe_Temperatur()
Temp_Farbe()