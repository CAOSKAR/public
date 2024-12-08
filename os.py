import os
import datetime
from datetime import timedelta
path = r"C:\Users\oezka\AppData\Local\Programs\Python\programdir"

for file in os.listdir(path):
    # Zeitpunkt der Dateiaenderung unformatiert
    dt_m = datetime.datetime.fromtimestamp(os.path.getmtime(path),)

    #dt_f = datetime.strftime(dt_m, '%d-%m-%Y %H:%M:%S')
    dt_f = dt_m.strftime("%d.%m.%Y %H:%M:%S")

    # aktuelle Zeit unformatiert
    dt_c = datetime.datetime.now()#.strftime("%d.%m.%Y %H:%M:%S")

    # aktuelle Zeit formatiert
    dt_cf = dt_c.strftime("%d.%m.%Y %H:%M:%S")
    #print (type(dt_bdt))
    #print (type(dt_end))
    #print (type(dt_tt))

    # Zeitpunkt der Dateierstellung unformatiert
    dt_b = datetime.datetime.fromtimestamp(os.path.getctime(path))

    # Zeitpunkt der Dateierstellung formatiert
    dt_f = dt_b.strftime("%d.%m.%Y %H:%M:%S")

    # calculating end date by adding 10 days 
    dt_end = dt_c + timedelta(days=-90) 
    dt_endf = dt_end.strftime("%d.%m.%Y %H:%M:%S")
  
    print('Letzte Dateiaenderung:', dt_m)
    print('Die Dateierstellung:', dt_b)
    print('Die Dateierstellung formatiert:', dt_f)
    print('Die aktuelle Zeit unformatiert:', dt_c
          )
    print('Die aktuelle Zeit formatiert:', dt_cf)
    print('Die aktuelle Zeit -90 Tage unformatiert:', dt_end)
    print('Die aktuelle Zeit -90 Tage formatiert:', dt_endf)
    print("Der Pfad ist",path)
    print(f"Path is {path}")




