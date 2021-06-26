import time

#Auswerten der Messdaten von ID 0001 und bereitstellen der Daten auf der Website
while 1:
    Messdaten = []

    #auslesen des txt Dokuments
    txt = open("/home/pi/Documents/Datenbanken/0001.txt", "r")
    for line in txt:
        Messdaten.append(line)
    txt.close()

    Aktuelste_Messung = Messdaten[-1]
    #bsp. für Aktuelste_Messung: ['2021', '06', '06', '09', '49', '33']#M12.4M12.5

    Datum = Aktuelste_Messung.replace("'","").split(",")[1:5]
    Datum = "%s.%s. %s:%s"%(Datum[0], Datum[1], Datum[2], Datum[3])

    Messung = Aktuelste_Messung.split("#")[1]
    Messung = Messung.split("M")[1:]
    #Zeilenumbruch am ende entfernen
    Messung[1] = Messung[1][0:len(Messung[1])-1]


    #schreiben auf "Aktuele Messung" html Seite
    html = open("/var/www/html/Wasser Station.html", "w")

    html.write("""  <!DOCTYPE html>
                    <html lang=de dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="style.css", type="text/css">
                        <link rel="icon" type="image/png" href="Bilder/icon.png" sizes="96x96">
                        <title>Wasser Station</title>
                      </head>
                      <body>
                        <div id="menü_gesamt">
                          <a href="index.html"><img src="Bilder/Logo.png" alt="Logo" height="75px" id="menü_logo"></a>
                          <table id="menü_tabelle">
                            <tr>
                              <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="#.html">AKTUELL</td>
                              <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="Vergangene Wassermessungen.html">VERGANGENE</td>
                    
                            </tr>
                          </table>
                        </div>
                        <div id="seiteninhalt">
                          <h1>Wasser Temperatur Aktuell</h1>
                          <br><br><br>
                          <p class="wasser_temperatur">In 20cm Tiefe: %s°</p>
                          <p class="wasser_temperatur">In 1m Tiefe: %s°</p>
                          <p id="label_letzte_aktualisierung">zuletzt aktual.:%s</p>
                        </div>
                    
                      </body>
                    </html>
"""%(Messung[0], Messung[1], Datum))

    html.close()

    #bereitstellen der Vergangenen Messwerte
    
    htmlschrift_Vergangene_Messungen = """"""
    
    #umdrehen der Messwerte um neuste zu erst zubearbeiten
    Messdaten = Messdaten[::-1]

    for messung in Messdaten:
        Datum = messung.replace("'","").split(",")[1:5]
        Datum = "%s.%s. %s:%s"%(Datum[0], Datum[1], Datum[2], Datum[3])
        
        Messung = messung.split("#")[1]
        Messung = Messung.split("M")[1:]
        #Zeilenumbruch am ende entfernen
        Messung[1] = Messung[1][0:len(Messung[1])-1]
        
        htmlschrift_Vergangene_Messungen += """<tr>
                                                  <td class="Vergangene_Wassermessungen_Tabelle_Spalte">%s</td>
                                                  <td class="Vergangene_Wassermessungen_Tabelle_Spalte">%s°</td>
                                                  <td class="Vergangene_Wassermessungen_Tabelle_Spalte">%s°</td>
                                               </tr>"""%(Datum, Messung[0], Messung[1])

    html = open("/var/www/html/Vergangene Wassermessungen.html", "w")

    html.write("""  <!DOCTYPE html>
                    <html lang=de dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="style.css", type="text/css">
                        <link rel="icon" type="image/png" href="Bilder/icon.png" sizes="96x96">
                        <title>Wasser Station</title>
                      </head>
                      <body>
                        <div id="menü_gesamt">
                          <a href="index.html"><img src="Bilder/Logo.png" alt="Logo" height="75px" id="menü_logo"></a>
                          <table id="menü_tabelle">
                            <tr>
                              <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="Wasser Station.html">AKTUELL</td>
                              <td class="menü_tabellen_spalte"><a class ="menü_tabellen_element" href="#">VERGANGENE</td>
                    
                            </tr>
                          </table>
                        </div>
                        <div id="seiteninhalt">
                          <h1>Vergangene Messungen</h1>
                        </div>
                    
                        <table id="Vergangene_Wassermessungen_Tabelle">
                          <tr>
                            <th class="Vergangene_Wassermessungen_Tabelle_Kopf">Datum/Uhrzeit</th>
                            <th class="Vergangene_Wassermessungen_Tabelle_Kopf">20cm</th>
                            <th class="Vergangene_Wassermessungen_Tabelle_Kopf">1m</th>
                          </tr>
                          %s
                        </table>
                    
                      </body>
                    </html>"""%htmlschrift_Vergangene_Messungen)
    html.close()
    time.sleep(60)
