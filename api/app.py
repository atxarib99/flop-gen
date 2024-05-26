from connexion import FlaskApp
import sys
import os
import importlib
import inspect
from engine import engine
import engine.filters
import pkgutil


app = FlaskApp("flop-gen")

app.add_api("openapi.yaml", dir='./')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)

def get_filters():
    filter_out = []
    filters_path = os.path.dirname(engine.filters.__file__)
    filters = [(loader,name,ispkg) for loader, name, ispkg in pkgutil.iter_modules([filters_path])]
    #for all filters in pkg engine.filters.*
    for filter in filters:
        #ignore abstract class
        if filter[1] == 'filter':
            continue
        #load modules
        _module = importlib.import_module('{}.{}'.format('engine.filters', filter[1]))
        #for each member in module
        for name, obj in inspect.getmembers(_module):
            #ensure its a class
            if inspect.isclass(obj):
                #skip filters.filter.Filter
                if "Filter" in name:
                    continue
                this_filter = {}
                this_filter['name'] = name
                this_filter['description'] = 'todo'
                this_filter['options'] = obj.options
                filter_out.append(this_filter)

    return filter_out

def get_filter(name):
    # quick lil filter :)
    return list(filter(lambda x: x['name'] == name, get_filters()))

def generate(generateRequest):
    req_filters = generateRequest['filters']
    engine_parms = generateRequest['engine']

    #attempt to build each filter
    filters = []
    try:
        for filter in req_filters:
            filters.append(build_filter(filter['name'], filter['selection'], filter['inverted']))
            print(filters)
    except Exception as e:
        #todo: error msg
        print(e)
        return "ERROR"
        
    print(filters)
    output = engine.engine.generate(filters, engine_parms)

    print(output)
    return output

def build_filter(filter_name, option, inverted):
    module = importlib.import_module('engine.filters.' + filter_name)
    built = None
    #get the class
    for name, obj in inspect.getmembers(module):
        #ensure its a class that matches this name
        if inspect.isclass(obj):
            if name.lower() == filter_name.replace('_', ''):
                built = obj(option)
                if inverted:
                    built.invert()

    return built
