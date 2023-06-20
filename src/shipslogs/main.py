#!/usr/bin/env python3
from getpass import getuser
from time import sleep
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import loader
import datetime
#import horario
import ocr
import json
import subprocess 
import signal    
import sys    
#import getopt

#FAZER DEPOISSS RECEBER ARGUMENTOS
#PERGUNTAR PELO COMPRIMENTO
#pri = sys.argv[1]
argv = sys.argv
print(argv,"O QUE STOUA ESTUDAR")
opcs,args = (argv[1:],"h")
if "-h" in opcs:
    print("""
    ********************* Diário de Bordo ********************
    
            configurar paths,autor  : /home/dbordo/config.json
            configurar horarios     : /home/dbordo/horario.json
            
            opções: -h --help
                    -c --create   , ajuda a inserir horários

            Se no nome do fichiero tiver expressão regular 'ocr'
            vai ser adicionado a imagem e o texto

            """)
    quit()

if "-c" in opcs:
    os.system("dbordo_creator")
    quit()




#user
user = getuser()


#configs
with open('config.json') as json_file: 
    data = json.load(json_file)
# defenir diretorio default de entrada
if data['screenshot_input']=='':
    pics = f'/home/{user}/Pictures/'
else:
    pics = data['screenshot_input']

#diretorio default para guardar
if data['diary_output']=='': # FIXME
    pathpasta = f'/home/{user}/Documents/aulas'
else:
    pathpasta = data['diary_output']

#pathpasta+=data["diary_home"]
#cria a pasta da aulas se nao existir 
os.system('mkdir -p ' + pathpasta)


def getDayPath():
    datadodia = loader.getDay()
    if len(argv) > 1: 
        topic = argv[1]
    else:
        topic = 'default'
    return os.path.join(pathpasta,topic,datadodia)

#event logger
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
     
        # FINAL PATH /home/jotaalvim/Documents/aulas/lalalal/2023-6-18/
        base = getDayPath()
        images = os.path.join(base,'images')
        if not os.path.exists(base):
            os.system(f'mkdir -p {base}')
            os.system(f'mkdir -p {images}')
            
        #nome da nova foto
        _,fc = os.path.split(event.src_path)

        FIXME ACABAR IMAGens

        n = 1
        nomes = ""

        # FIXME mudar o nome
        ver = os.path.join(base,fc)
        print(ver)
        while os.path.exists(ver):
            nome = fc.split('.')
            tipo = nome.pop()
            nome1 = nome
            nome = ""
            for i in nome:
                nomes += i+"."
            nomes = nomes[:-1]
            fc = f"{nome1}-{n}."+tipo
            n+=1

        # mover para o novo sitio
        sleep(1)
        pathinput  = event.src_path 
        pathoutput = os.path.join(images,fc)
        subprocess.run(["mv",pathinput,pathoutput])
        # adicionado ficheiro de texto
        # obtem texto
        sleep(1)
        ocr.inseretexto(base,fc)
   

def handler(sig, frame):
    print(
"""\n======================================
Handler Final que trata das converções
======================================""")
    path = getDayPath()
  
    dbpdf = os.path.join(path,"dbordo.pdf")
    dbhtml = os.path.join(path,"dbordo.html")
    dbmd = os.path.join(path,"Diario_de_bordo.md")
    os.system(f"pandoc -t latex -o {dbpdf} {dbmd}")
    os.system(f"pandoc {dbmd} -V fontsize=12pt -V geometry:margin=1in -o {dbhtml}")
    
    sys.exit(0)


if __name__ == "__main__":
    
    signal.signal(signal.SIGINT, handler)
    #signal.alarm(0)
    
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
