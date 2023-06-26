import json
import os

#lectura de datos json
def read_json():
    if not os.path.isfile('data.json'):
        with open('data.json', 'W') as f:
            json.dump([],f)
    with open('data.json','r') as f:
        data= json.load(f)
    return data

#escritura para agregar al archivo Json
def write_json(data):
    with open('data.json','w')as f:
        json.dump(data,f)