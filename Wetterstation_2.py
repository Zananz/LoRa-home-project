#ID 0000
#um Daten auf einer Webside zur verfügung zu stellen

import time

while 1:
    #Daten der letzten messung auslesen
    txt = open("/home/pi/Documents/Datenbanken/0000.txt", "r")

    #letzte zeile im txt auslesen
    for line in txt:
        pass

    letzer_eintrag = line 

    txt.close()

    #herausfinden de Zeit/ der Daten
    letzer_eintrag = letzer_eintrag.split("#")

    datum = letzer_eintrag[0]
    daten = letzer_eintrag[1]

    # datum in gewünschtes format:
    datum = datum.replace("[","").replace("]","").replace("'","").replace(" ","")
    datum = datum.split(",")
    datum = "%s.%s. %s:%s"%(datum[2],datum[1],datum[3],datum[4])

    #werte der luftfeuchtigkeit und der temperatur auslesen
    daten = daten.replace("T","").split("L")
    temperatur = daten[0]
    luftfeuchte = daten[1]

    #werte in .html schreiben
    html = open("/var/www/html/Luft Station.html", "w")
    html.write("""
    <!DOCTYPE html>
    <html lang=de dir="ltr">
      <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="style.css", type="text/css">
        <link rel="icon" type="image/png" href="Bilder/icon.png" sizes="96x96">
        <title>Wetter</title>
      </head>
      <body>
        <div id="menü_gesamt">
        <a href="index.html"><img src="Bilder/Logo.png" alt="Logo" height="75px" id="menü_logo"></a>
        <table id="menü_tabelle">
          <tr>
            <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="#">AKTUELL</td>
            <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="Vergangene Messungen.html">VERGANGENE</td>

          </tr>
        </table>
      </div>
      <div id="seiteninhalt">
        <h1>Aktuell</h1>
        <p id="temperatur_luft">%s°</p>
        <p id="luftfeuchtigkeit">@%s%%</p>
        <p id="label_letzte_aktualisierung">zuletzt aktual.:%s</p>
      </div>
      </body>
    </html>"""%(temperatur, round(float(luftfeuchte)), datum))#luftfeuchtigkeit runden da optisch besser u. genau. 5%
    html.close()
    
    #bereitstellen der vergangenen messungen
    #aktionen wiederholen sich (übersicht)
    
    messungen = []
    #Daten der messung auslesen
    txt = open("/home/pi/Documents/Datenbanken/0000.txt", "r")
    
    for line in txt:
        messungen.append(line)
        
    txt.close()
    
    #aufbereiten der Daten
    messungen_zwischenspeicher = messungen
    messungen = []
    
    for messung in messungen_zwischenspeicher:
        
        messung = messung.split("#")

        datum = messung[0]
        daten = messung[1]

        # datum in gewünschtes format:
        datum = datum.replace("[","").replace("]","").replace("'","").replace(" ","")
        datum = datum.split(",")
        datum = "%s.%s.&nbsp;%s:%s"%(datum[2],datum[1],datum[3],datum[4])#&nbsp; wichtig in html um Zeilenumbruch auf Mobilen Geräten zu verhindern

        #werte der luftfeuchtigkeit und der temperatur auslesen
        daten = daten.replace("T","").split("L")
        temperatur = daten[0]
        luftfeuchte = daten[1]
        
        messungen.append([datum, temperatur, luftfeuchte])
    
    #werte sollen in tabellenform in html geschriben werden
    html_schrift = ""
    
    messungen = messungen[:len(messungen)-1]#entfernen der letzten messung
    
    messungen = messungen[::-1]#um neuste messungen vorn zu sehen
    
    for messung in messungen:
        
        try: #fehler nach letzter zeile... effektivste lösung
            html_schrift += """<tr class="h24_tabelle_reihe">
                                <td class = "h24_tabelle_datum">%s</td>
                                <td class = "h24_tabelle_werte">%s°&nbsp;%s%%</td>
                            </tr>"""%(messung[0], messung[1], round(float(messung[2])))#messung 2 runden(luftfeuchtigkeit) da optisch besser u. genau. 5%
        except:
            pass
    
    #schreiben in die .html datei
    html = open("/var/www/html/Vergangene Messungen.html", "w")
    
    html.write("""
    <!DOCTYPE html>
    <html lang=de dir="ltr">
      <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="style.css", type="text/css">
        <link rel="icon" type="image/png" href="Bilder/icon.png" sizes="96x96">
        <title>Tepmeratur</title>
    
      </head>
      <body>
        <div id="menü_gesamt">
        <a href="index.html"><img src="Bilder/Logo.png" alt="Logo" height="75px" id="menü_logo"></a>
        <table id="menü_tabelle">
          <tr>
            <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="Luft Station.html">AKTUELL</td>
            <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="#">VERGANGENE</td>
    
          </tr>
        </table>
      </div>
      <div id="seiteninhalt">
        <h1>VERGANGENE MESSUNGEN</h1>
        <table id = "h24_tabelle">
          %s
        </table>
      </div>
      </body>
    </html>"""%html_schrift)
    
    html.close()
        
    time.sleep(60)
