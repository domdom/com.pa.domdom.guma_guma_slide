import json
import os
import platform
import re
import collections



def data_dir():
    path = 'unknown'
    if platform.system() == 'Windows':
        path = os.path.normpath(os.path.join(os.getenv('USERPROFILE'), "AppData\\local\\Uber Entertainment\\Planetary Annihilation"))
        
    if platform.system() == 'Linux':
        path = os.path.normpath(os.path.join(os.getenv('HOME'), ".local/Uber Entertainment/Planetary Annihilation"))
        
    if platform.system() == 'Darwin':
        path = os.path.normpath(os.path.join(os.getenv('HOME'), "Library/Application Support/Uber Entertainment/Planetary Annihilation"))
    return path

def build():
    return "Unknown"

def mod_dir():
    path = os.path.dirname(__file__)
    print path
    

def pa_dir():
    log_dir = os.path.join(data_dir(), 'log/')
    for f in os.listdir(log_dir):
        if f.endswith(".txt"):
            log = open(os.path.join(data_dir(), 'log', f))

            for line in log:
                m = re.search(r'INFO Coherent host dir: "([^"]*)"', line)
                if m:
                    if platform.system() == 'Windows':
                        return os.path.normpath(os.path.join(m.group(1), '../../media'))
                    if platform.system() == 'Linux':
                        return os.path.normpath(os.path.join(m.group(1), '../../media'))
                    if platform.system() == 'Darwin':
                        return os.path.normpath(os.path.join(m.group(1), '../../Resources/media'))



mod_dir()

# loads a json file from the pa media directory
def load_base_json(path):
    if path[0] == '/':
        path = path[1:]
    path = os.path.join(pa_dir(), path)
    
    if os.path.exists(path):
        return json.load(open(path), object_pairs_hook=collections.OrderedDict)
    else: 
        return None

def load_mod_json(path):
    if path[0] == '/':
        path = path[1:]
    
    path = os.path.join(pa_dir(), path)
        
    if os.path.exists(path):
        return json.load(open(path), object_pairs_hook=collections.OrderedDict)
    else: 
        return None



