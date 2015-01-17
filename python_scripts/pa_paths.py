import os
import platform


def get_pa_data_dir():
    path = 'unknown'
    if platform.system() == 'Windows':
        path = os.path.join(os.getenv('USERPROFILE'), "AppData/local/Uber Entertainment/Planetary Annihilation")
        
    if platform.system() == 'Linux':
        path = os.path.join(os.getenv('HOME'), ".local/Uber Entertainment/Planetary Annihilation")
        
    if platform.system() == 'Darwin':
        path = os.path.join(os.getenv('HOME'), "Library/Application Support/Uber Entertainment/Planetary Annihilation")
    return path
    
def get_server_mod_dir():
    return  os.path.join(get_pa_data_dir(), 'server_mods')
    
def get_client_mod_dir():
    if os.path.exists(os.path.join(get_pa_data_dir(), 'mods')):
        return  os.path.join(get_pa_data_dir(), 'mods')
    if os.path.exists(os.path.join(get_pa_data_dir(), 'client_mods')):
        return  os.path.join(get_pa_data_dir(), 'client_mods')
