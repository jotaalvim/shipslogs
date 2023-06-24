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



def count_files(directory):
    file_count = 0
    for _, _, files in os.walk(directory):
        file_count += len(files)
    return file_count

def getNewName(oldPath,oldName):
    name = 'img-' + str(count_files(oldPath))
    if 'ocr' in oldName:
        name += '-ocr'
    name += '.png'
    return name