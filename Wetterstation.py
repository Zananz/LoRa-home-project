import time
import serial
import  matplotlib.pyplot as plt

import datetime
import csv

ser = serial.Serial(            
     port='/dev/ttyACM0',
     baudrate = 9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.FIVEBITS,
     timeout=610
 )
         
while 1:
    
    
    temp = str(ser.readline().decode())
    temp = float(temp.replace("'","").replace("b",""))
    temp = str(round(temp,1))
    print(temp)
    
    
    html = open("/var/www/html/index.html", "w")
    html.write("""  <!DOCTYPE html>
                    <html lang=de dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="style.css", type="text/css">
                        <title>Wetter</title>
                      </head>
                      <body>
                        <div id="menü_gesamt">
                        <img src="Bilder/Logo.png" alt="Logo" height="75px" id="menü_logo">
                        <table id="menü_tabelle">
                          <tr>
                            <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="#">AKTUEL</td>
                            <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="vergangene_24h.html">VERGANGENE 24h</td>

                          </tr>
                        </table>
                      </div>
                      <div id="seiteninhalt">
                        <h1>Aktuel</h1>
                        <p id="temperatur">25.5°</p>
                        <p id="luftfeuchtigkeit">@65%</p>
                        <p id="label_letzte_aktualisierung">zuletzt aktual.:21.06 20:00</p>
                      </div>
                      </body>
                    </html>

                    """%temp)
    html.close()
    
    datum = str(datetime.datetime.now()).replace(":","-").replace(" ","-").split("-")

    """with open('/home/pi/Documents/Temperaturdaten.csv', mode='a') as csv_file:
        fieldnames = ["jahr","monat","tag","stunde","minute","temperatur"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({"jahr" : datum[0],"monat" : datum[1],"tag" : datum[2],"stunde" : datum[3],"minute" : datum[4],"temperatur" : temp})
        del(writer)
        csv_file.close()"""
    
    with open('/home/pi/Documents/Temperaturdaten.csv', 'a') as csv:
        csv.write("%s,%s,%s,%s,%s,%s\n"%(datum[0],datum[1],datum[2],datum[3],datum[4],temp))

    alle_daten = []
    with open('/home/pi/Documents/Temperaturdaten.csv', 'r') as csv:
        for i in csv :
            alle_daten.append(i)
    
        alle_daten = [i.strip() for i in alle_daten]
    
    länge = len(alle_daten)
    
    vergangene_24h = []
    
    for i in alle_daten:
        if alle_daten.index(i) > länge -146:
            vergangene_24h.append(i)
            
    vergangene_24h = [messung.split(",") for messung in vergangene_24h]
    
    
    datum = []
    temperatur = []
    
    for messung in vergangene_24h:
        datum.append("%s:%s"%(messung[3],messung[4] if int(messung[4]) != 0 else "00"))
        temperatur.append(round(float(messung[5]),1))
        
    platzhalter = ""
    for i in datum:# unsichtbar machen (2 von 3) um überlapungen zu verhindern
        if datum.index(i) % 3 != 1:
            pos = datum.index(i)
            datum.pop(pos)
            datum.insert(pos,platzhalter)
    
            platzhalter += " "
    
    plt.figure(figsize=(17,7))
    plt.plot(datum,temperatur, color = ("#4444FF") )
    plt.xlabel("Uhrzeit", fontsize = 20,color=("#AAAAAA"))
    plt.ylabel("Temperatur in °C",fontsize = 20,color=("#AAAAAA"))
    plt.grid()
    plt.xticks(rotation=30)
    
    plt.savefig(fname="/var/www/html/Bilder/graph_vergangene_24h.png")
    
