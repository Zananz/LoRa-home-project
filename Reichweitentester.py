import time
while 1:
    txt = open("/home/pi/Documents/Datenbanken/0003.txt", "r")

    for line in txt:
        pass
    try:
        last = line
        txt.close()
        open("/home/pi/Documents/Datenbanken/0003.txt", "w").close()

        html = open("/var/www/html/Debug/tester.html","w")
        html.write("""  <!DOCTYPE html>
                        <html lang="de" dir="ltr">
                            <head>
                                <meta charset="utf-8">
                                <title>Debug help</title>
                            </head>
                            <body>
                                %s
                            </body>
                        </html>"""%last)
        html.close()
    except:
        pass
    time.sleep(10)
