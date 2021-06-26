import serial
import time
import datetime

print("Gateway gestartet...")

ser = serial.Serial(            
     port='/dev/ttyACM0',
     baudrate = 9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.FIVEBITS,
     timeout=10000
)
def Datenbank_eintrag(liste):
    
    for element in liste:
        
        print(element)
        
        #herausfiltern der Netz ID
        Netz_ID = element[:4]
        print(Netz_ID)
        #speichern der Daten in einer .txt Datei (eigene für jede ID)
        #mit Zeitstempel
        txt = open("/home/pi/Documents/Datenbanken/%s.txt"%Netz_ID, "a")
        
        #datum als str ["yyyy", "mm", "dd", "hh", "minmin", "ss"]
        datum = str(str(datetime.datetime.now()).replace("-",":").replace(".",":").replace(" ",":").split(":")[:6])
        
        #eintrag in zeilenform im txt doku.
        txt.write("%s#%s\n"%(datum, element[4::]))
        
        txt.close()
        
        #schreiben in das Backup
        txt = open("/media/pi/USB/Backup/%s.txt"%Netz_ID, "a")
        
        #datum als str ["yyyy", "mm", "dd", "hh", "minmin", "ss"]
        datum = str(str(datetime.datetime.now()).replace("-",":").replace(".",":").replace(" ",":").split(":")[:6])
        
        #eintrag in zeilenform im txt doku.
        txt.write("%s#%s\n"%(datum, element[4::]))
        
        txt.close()
    
    
while 1:
    
    in_come = ser.readline()
    
    print(in_come)
    
    #filtern der ungewollt mitgeliferten daten
    in_come = "%s"%in_come
    in_come = in_come[4:len(in_come)-6]
    print(in_come)
    
    in_come = in_come.split("Zananz")
    
    in_come = in_come[1:]#erstes element nie wichtig
    
    Datenbank_eintrag(in_come)
    """
    if in_come[:6] == "Zananz":#"Zananz" fungirt als Netz Audenifizirung
        
        in_come = in_come[6::]
        
        #herausfiltern der Netz ID
        Netz_ID = in_come[:4]
        
        #speichern der Daten in einer .txt Datei (eigene für jede ID)
        #mit Zeitstempel
        txt = open("/home/pi/Documents/Datenbanken/%s.txt"%Netz_ID, "a")
        
        #datum als str ["yyyy", "mm", "dd", "hh", "minmin", "ss"]
        datum = str(str(datetime.datetime.now()).replace("-",":").replace(".",":").replace(" ",":").split(":")[:6])
        
        #eintrag in zeilenform im txt doku.
        txt.write("%s#%s\n"%(datum, in_come[4::]))
        
        txt.close()"""
        
        
    time.sleep(1)