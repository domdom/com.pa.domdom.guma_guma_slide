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

def pa_dir():
    log_dir = os.path.join(data_dir(), 'log/')
    for f in os.listdir(log_dir):
        if f.endswith(".txt"):
            log = open(os.path.join(data_dir(), 'log', f))

            for line in log:
                m = re.search(r'INFO Coherent host dir: "([^"]*)"', line)
                if m:
                    return os.path.normpath(os.path.join(m.group(1), '../../media'))


print pa_dir()

# loads a json file from the pa media directory
def load_base_json(path):
    if path[0] == '/':
        path = path[1:]
    return json.load(open(os.path.join(pa_dir(), path)), object_pairs_hook=collections.OrderedDict)

def load_mod_json(path):
    if path[0] == '/':
        path = path[1:]

print load_base_json('/pa/units/unit_list.json')


