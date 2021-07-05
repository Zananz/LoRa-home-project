import time

with open("/home/pi/Documents/Datenbanken/0004.txt", "r") as txt:
    
    for line in txt:
        pass

if line == "0":
    pass

else:
    letzer_eintrag = line.split("#")

    datum = letzer_eintrag[0]
    daten = letzer_eintrag[1]

    datum = datum.replace("[","").replace("]","").replace("'","").replace(" ","")
    datum = datum.split(",")
    datum = "%s.%s. %s:%s"%(datum[2],datum[1],datum[3],datum[4])
    
    daten = list(daten)
    
    software = daten[0]
    hardware = daten[1]
    
    if software == 0:
        software = "Offen"
    else:
        software = "Geschlossen"
        
    if hardware == 0:
        hardware = "Offen"
    else:
        hardware = "Geschlossen"
            
    with open("/var/www/html/Hühnerklappe.html", "w") as txt:
        
        txt.write("""<!DOCTYPE html>
<html lang="de" dir="ltr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css", type="text/css">
  <link rel="icon" type="image/png" href="Bilder/icon.png" sizes="96x96">
  <title>Sensor Stationen</title>
</head>
  <body>
    <div id="menü_gesamt">
      <a href="index.html"><img src="Bilder/Logo.png" alt="Logo" height="75px" id="menü_logo"></a>
    </div>
    <div id="seiteninhalt">
      <h1>Hühnerklappe</h1>
      <br><br><br><br><br><br>
      <p class = "Zustand_Klappe">Laut Software: %s</p>
      <p class = "Zustand_Klappe">Laut Hardware: %s</p>
      <p id="label_letzte_aktualisierung">zuletzt aktual.: %s</p>
    </div>
  </body>
</html>"""%(software, hardware, datum))
        
    with open("/home/pi/Documents/Datenbanken/0004.txt", "w") as txt:
        txt.write("0\n")
        
time.sleep(60)
