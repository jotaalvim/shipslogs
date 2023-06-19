import os
import datetime
import json
#import horario

#devolve o último ficheiro editado na diretoria dos screenshots
def up(path):
    # return os.system("ls -t /home/" + user + "/Pictures  |  head -n1")
    name_list = os.listdir(path)
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)

    sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
    return sorted_filename_list[-1]#último elemtnos da lista, ficheiro mais recente



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
