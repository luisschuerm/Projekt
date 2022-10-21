from GPIO import LED,Sensor,LCD,Luefter
import time
Gruen = LED ("gruen")
Gruen.aus()
Gelb = LED ("gelb")
Gelb.aus()
Rot = LED ("rot")
Rot.aus()
Lüfter = Luefter()
display = LCD()
SEN = Sensor ("28-00000a2aa46c")
"""
x = 1
while x < 10:    
        Gruen.an()
        time.sleep(2)
        Gruen.aus()
        Gelb.an()
        time.sleep(2)
        Gelb.aus()
        Rot.an()
        time.sleep(2)
        Rot.aus()
        Lüfter.aus()
        x= x + 1

for j in range(1):
    
    time.sleep(2)
    Werte = float(SEN.lesen())
    display.schreiben("  "+str(Werte)+" C",1)
    print(Werte)
    
    if Werte <20:
      display.loeschen()
      display.schreiben("  "+str(Werte)+" C",1)
      display.schreiben("Kalt",2)
      Lüfter.aus()
      Rot.aus()
      Gelb.aus()
      Gruen.an()

    elif Werte >20 and Werte <30:
      display.loeschen()
      display.schreiben("  "+str(Werte)+" C",1)
      display.schreiben("Warm",2)
      Lüfter.aus()
      Rot.aus()
      Gelb.an()
      Gruen.aus()
      
    elif Werte > 30:
      display.loeschen()
      display.schreiben("  "+str(Werte)+" C",1)
      display.schreiben("Heiß",2)
      Lüfter.aus()
      Rot.an()
      Gelb.aus()
      Gruen.aus()

while True:
    Farbe = input("Bitte hier deine Farbe eingeben ")
    
    if Farbe == "Grün" or Farbe == "Gruen" or Farbe == "grün" or Farbe == "gruen":
      Rot.aus()
      Gelb.aus()
      Gruen.an()
      Lüfter.aus()
    
    elif Farbe == "Gelb" or Farbe == "gelb":
      Rot.aus()
      Gelb.an()
      Gruen.aus()
      Lüfter.aus()
    
    elif Farbe == "Rot" or Farbe == "rot":
      Rot.an()
      Gelb.aus()
      Gruen.aus()
      Lüfter.aus()
    
    elif Farbe == "Exit" or Farbe == "exit":
      print("Tschöö mit ö")
      Rot.aus()
      Gelb.aus()
      Gruen.aus()
      Lüfter.aus()
      break


max = float(input("Bitte hier das Maximum eingeben: "))
min = float(input("Bitte hier das Minimum eingeben: "))
   
for i in range(1):
    Werte = float(SEN.lesen())
    print(Werte)
    
    if Werte < min:
        display.loeschen()
        display.schreiben("Kalt",1)
        Rot.aus()
        Gelb.aus()
        Gruen.an()
        Lüfter.aus()
    
    elif Werte > min and Werte < max:
        display.loeschen()
        display.schreiben("Warm",1)
        Rot.aus()
        Gelb.an()
        Gruen.aus()
        Lüfter.aus()

    elif Werte >max:
        display.loeschen()
        display.schreiben("Heiß",1)
        Rot.an()
        Gelb.aus()
        Gruen.aus()
        Lüfter.aus()

for k in range(3):
    Gruen.an()
    Gelb.an()
    time.sleep(2)
    Gelb.aus()
    Rot.an()
    time.sleep(2)
    Gruen.aus()
    Gelb.an()
    time.sleep(2)
    Gruen.aus()
    Gelb.aus()
    Rot.aus()
    time.sleep(5)
    Rot.an()
    Gelb.an()
    Gruen.an()
    time.sleep(2)
    Gelb.aus()
    Gruen.aus()
    Rot.aus()
    display.loeschen()
    Lüfter.aus()

"""
while True:
    Werte = float(SEN.lesen())
    
    if Werte > 20:
        Lüfter.an()
        
    else:
        Lüfter.aus()

     