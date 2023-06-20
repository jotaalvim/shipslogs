import os
import datetime
import json
#import horario


with open('config.json') as json_file: 
    data = json.load(json_file)

def getDay():
    #horas a que foi criado
    now = datetime.datetime.now()
    today = ""

    dia, mes, ano = str( now.day), str( now.month), str( now.year)
    ordem = (data["date_format"]).split('/')
    for i in ordem:
        ##YY/MM/DD
        if "YY"==i:
            today+=ano+"-"
        elif "MM"==i:
            today+=mes+"-"
        else:
            today+=dia+"-"
    return today[:-1]
