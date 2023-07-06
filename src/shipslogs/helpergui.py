import json


def toogleFormat(format):
    with open('config.json') as json_file: 
        data = json.load(json_file)

    print( data['export_formats'])
    data['export_formats'][format] = not data['export_formats'][format] 
    print( data['export_formats'])

    with open('config.json', 'w') as jsonFile:
        json.dump(data, jsonFile)


def setFormat(format):
    with open('config.json') as json_file: 
        data = json.load(json_file)

    return data['export_formats'][format]
    

def getSettings():
    with open('config.json') as json_file: 
        data = json.load(json_file)

    # FIXME devia usar isto na main 
    # e ver se os paths sao validos
    if data['author_name'] == '':
        name = getuser()
    else:
        name = data['author_name']  

    return (name, data['diary_output'], data['screenshot_input'],data['date_format'])

def setSettings(info):
    with open('config.json') as json_file: 
        data = json.load(json_file)
    
    a,o,i,f = info
    #FIXME
    if a != '':
        data['author_name'] = a
    if o != '':
        data['diary_output'] = o
    if i != '':
        data['screenshot_input'] = i
    if f != '':
        data['date_format'] = f

    with open('config.json', 'w') as jsonFile:
        json.dump(data, jsonFile)
