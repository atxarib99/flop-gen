from connexion import FlaskApp
import sys
import os
import importlib
import inspect
import engine as engine
from filters import * 

app = FlaskApp("flop-gen")

app.add_api("openapi.yaml", dir='./')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)

def get_filters():
    #get modules in engine.filters and return in proper format
    current_module = sys.modules['engine']
    print(current_module.__class__('Texture'))
    filters = []
    act_filters = []
    for item in os.listdir('./filters/'):
        if item.endswith('.py'):
            #exclude abstract class
            if item == 'filter.py':
                continue

            #exclude hidden
            if "__" in item:
                continue
            print(item)
            filters.append(importlib.import_module('filters.' + item[0:-3], item[0:-3]))
            print(filters[-1])
            for name, obj in inspect.getmembers(filters[-1]):
                if inspect.isclass(obj):
                    #skip Card.py dep
                    if "Card" in name:
                        continue
                    #skip filters.filter.Filter
                    if "filter.Filter" in name:
                        continue

                    act_filters.append(obj)
                    print(act_filters[-1].options)


    return [{'name': 'texture', 'description': 'Flop texture', 'options': ['rainbow', 'two tone', 'monotone']}]

def get_filter(name):
    #get modules in engine.filters, find labeled 'name', return or 404
    return {'name': name, 'description': 'Flop texture', 'options': ['rainbow', 'two tone', 'monotone']}

def generate(generateRequest: str):
    return None
