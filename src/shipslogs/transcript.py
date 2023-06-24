import os
import datetime
from ocr import *
from main import handler
path = "/home/jotaalvim/Documents/aulas/lalalal/2023-6-24/images"

def transcribe(input,output):

    #================================================================================
    # Fazer pastas output
    os.system(f'mkdir -p {output}')
    #================================================================================
    
    for root, _, files in os.walk(input, topdown=True):
        file_paths = []
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
            ocrt = gettext(file)
            #print(ocrt)
            aula = open(dbordo,'a')
            aula.write(f"\n![]({file})\n")
            aula.write(f"\n```\n{ocrt}\n```\n")
            #aula.write("\n---\n")
        else:
            aula = open(dbordo,'a')
            aula.write(f"\n![]({file})\n")
            #aula.write("\n---\n")
        aula.close()
    handler(1,1,output)

transcribe(path,'ola')
