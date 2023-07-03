import json


def toogleFormat(format):
    with open('config.json') as json_file: 
        data = json.load(json_file)

    print( data['export_formats'])
    data['export_formats'][format] = not data['export_formats'][format] 
    print( data['export_formats'])

    with open('config.json', 'w') as jsonFile:
        json.dump(data, jsonFile)


def set(format):
    with open('config.json') as json_file: 
        data = json.load(json_file)

    return data['export_formats'][format]
    
