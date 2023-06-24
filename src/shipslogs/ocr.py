import datetime
import pytesseract
from PIL import Image
import os
from mdutils.mdutils import MdUtils
from mdutils import Html
import json
from getpass import getuser

with open('config.json') as json_file:
    data = json.load(json_file)

if data["author_name"]=="":
    user=getuser()
else:
    user=data["author_name"]


def gettext(path): # devolve texto de uma imagem de algum lado
    return pytesseract.image_to_string(Image.open(path),lang = 'por+eng')


def inseretexto(path,fich,new): # dado o diretorio da pasta adiciona ao texto.txt
    dbordo = os.path.join(path,'Diario_de_bordo.md')
    ff = os.path.join(path,'images',new)

    if not os.path.exists(dbordo):
        aula = open(dbordo,'a')
        x = datetime.datetime.now()
        ano = x.year
        mes = x.strftime("%B")
        dia = x.day
        aula.write(f'---\ntitle: \"Ship\'s Logs\"\nauthor: {user} \ndate: {mes} {dia}, {ano}\ngeometry: margin=2cm\noutput: pdf_document\nfontsize: 100pt\n---\n')
        aula.close()
        #inseretexto(path,fich)


    #if os.path.exists(dbordo):
        # fich "ocr.pdf"
                
    if "ocr" in fich:
        ocrt = gettext(ff)
        aula = open(dbordo,'a')
        aula.write(f"\n![]({ff})\n")
        aula.write(f"\n```\n{ocrt}\n```\n")
        #aula.write("\n---\n")
    else:
        aula = open (dbordo,'a')
        aula.write(f"\n![]({ff})\n")
        #aula.write("\n---\n")
    aula.close()

 
