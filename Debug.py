#debughilft (anzeige wann  Pyboard zuletzt gesehen wurde)

import time

while True:
    txt = open("/home/pi/Documents/Datenbanken/0002.txt", "r")
    #herauslesen der letzen Zeile
    for line in txt:
        pass

    last_seen = line

    txt.close()

    #löschen älterer einträge um nicht unnötig speicher zu verschenden
    open("/home/pi/Documents/Datenbanken/0002.txt", "w").close()

    date = last_seen.split("#")[0].replace("'","").replace("[","").replace("[","").split(",")
    date = "Pyboard zu letzt am %s.%s.%s um %s:%s gesehen."%(date[2], date[1], date[0], date[3], date[4])

    html = open("/var/www/html/Debug/index.html", "w")

    html.write("""  <!DOCTYPE html>
                    <html lang="de" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>Debug help</title>
                      </head>
                      <body>
                        %s
                      </body>
                    </html>
    """%date)
    html.close()
    time.sleep(61)#61um dauerhafte deckung zu vermeiden
