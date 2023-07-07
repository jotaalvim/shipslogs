#!/usr/bin/env python3

from getpass import getuser
from time import sleep
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from loader import getDay,getNewName

import datetime
import ocr
import json
import subprocess
import signal
import sys

#FAZER DEPOISSS RECEBER ARGUMENTOS
#PERGUNTAR PELO COMPRIMENTO
#pri = sys.argv[1]
argv = sys.argv

opcs,args = (argv[1:],"h")

if "-h" in argv:
    print("""
    ********************* Ship's Logs ********************
    
            configurar paths,autor  : /home/dbordo/config.json
            
            options: -h --help

            
            if the words 'ocr' is in the image name then a ocr operation 
            to transcript the text will be made

            """)
    quit()



#user
user = getuser()


#configs
with open('config.json') as json_file: 
    data = json.load(json_file)
# defenir diretorio default de entrada
if data['screenshot_input']=='':
    pics = os.path.join('home',user,'Pictures') #pics = f'/home/{user}/Pictures/'
else:
    pics = data['screenshot_input']

#diretorio default para guardar
if data['diary_output']=='': # FIXME
    pathpasta = os.path.join('home',user,'Documents','hipslogss') #pathpasta = f'/home/{user}/Documents/aulas'
else:
    pathpasta = data['diary_output']



#pathpasta+=data["diary_home"]
#cria a pasta de outrput topic se nao existir
os.system('mkdir -p ' + pathpasta)




def getDayPath(datadodia=getDay()):
    #datadodia = getDay()
    if len(argv) > 1: 
        topic = argv[1]
    else:
        topic = 'default'
    return os.path.join(pathpasta,topic,datadodia)

#event logger
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
     
        # FINAL PATH /home/jotaalvim/Documents/aulas/lalalal/2023-6-18/
        if len(argv) == 3:
            # cria uma subpasta com um nome passado por arumento
            # em vez do dia
            base = getDayPath(argv[-1])
        else:
            base = getDayPath()

        print(base)

        images = os.path.join(base,'images')
        if not os.path.exists(base):
            os.system(f'mkdir -p {base}')
            os.system(f'mkdir -p {images}')
        
        #fc = nome atnigo da nova foto
        _,fc = os.path.split(event.src_path)

        newName = getNewName(images,fc)
        pathinput  = event.src_path
        pathoutput = os.path.join(images,newName)

        sleep(0.5)
        subprocess.run(["mv",pathinput,pathoutput])
        sleep(1)
        ocr.inseretexto(base,fc,newName)


def handler(sig, frame,path=getDayPath()):
    print(
"""\n======================================
Exporting diary
======================================""")

    if path == getDayPath() and len(argv) == 3:
        # cria uma subpasta com um nome passado por arumento
        # em vez do dia
        path = getDayPath(argv[-1])
    elif path == getDayPath():
        path = getDayPath()

    with open('config.json') as json_file: 
        data = json.load(json_file)

    dbmd = os.path.join(path,'Diario_de_bordo.md')
    dfor = data['export_formats']
    for format in dfor.keys():
        if dfor[format]:
            diary = os.path.join(path,"shipslogs."+format)
            print(diary)
            os.system(f'pandoc -o {diary} {dbmd}')
    
    sys.exit(0)


def transcript2(input,output):
    print(input,output)
    #================================================================================
    # Fazer pastas output
    os.system(f'mkdir -p {output}')
    #================================================================================
    file_paths = []
    for root, _, files in os.walk(input, topdown=True):
        
        for name in files:
           file_paths.append(os.path.join(root, name))


    sorted_file_paths = sorted(file_paths, key=os.path.getmtime)

    for file in sorted_file_paths:
        #print("adding ->",file)
        root,fname = os.path.split(file)
        dbordo = os.path.join(output,'Diario_de_bordo.md')

        if not os.path.exists(dbordo):
            aula = open(dbordo,'a')
            x = datetime.datetime.now()
            ano = x.year
            mes = x.strftime("%B")
            dia = x.day
            aula.write(f'---\ntitle: \"Ship\'s Logs\"\nauthor: {user} \ndate: {mes} {dia}, {ano}\ngeometry: margin=2cm\noutput: pdf_document\nfontsize: 100pt\n---\n')
            aula.close()

        if "ocr" in fname:
            ocrt = ocr.gettext(file)
            #print(ocrt)
            aula = open(dbordo,'a')
            aula.write(f"\n![]({file})\n")
            aula.write(f"\n```\n{ocrt}\n```\n")

        else:
            aula = open(dbordo,'a')
            aula.write(f"\n![]({file})\n")

        aula.close()
    handler(1,1,output)

if "-t" in argv:
    transcript2(argv[2],argv[3])
    quit()


if __name__ == "__main__":
    
    signal.signal(signal.SIGINT, handler)
    #signal.alarm(0)
    #init()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=pics, recursive=False)
    observer.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()