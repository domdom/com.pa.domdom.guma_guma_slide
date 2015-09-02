import os
import platform


def get_pa_data_dir():
    path = 'unknown'
    if platform.system() == 'Windows':
        path = os.path.join(os.getenv('USERPROFILE'), "AppData\\local\\Uber Entertainment\\Planetary Annihilation")
        
    if platform.system() == 'Linux':
        path = os.path.join(os.getenv('HOME'), ".local/Uber Entertainment/Planetary Annihilation")
        
    if platform.system() == 'Darwin':
        path = os.path.join(os.getenv('HOME'), "Library/Application Support/Uber Entertainment/Planetary Annihilation")
    return path
    
def get_server_mod_dir():
    return  os.path.normpath(os.path.join(os.path.basename(__file__), '..'))
