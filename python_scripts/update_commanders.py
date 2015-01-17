import os
import json

#root_part = os.path.abspath(os.sep)

pa_path = "C:\Games\Uber Entertainment\Planetary Annihilation Launcher\Planetary Annihilation\stable\media"

mod_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

print mod_path

unit_list_path = "C:\Games\Uber Entertainment\Planetary Annihilation Launcher\Planetary Annihilation\stable\media\pa\units\unit_list.json"

unit_list = json.load(open(unit_list_path))

for unit in unit_list['units']:
    if '/pa/units/commanders/' not in unit: continue
    if '/avatar/' in unit: continue

    # check if we have that commander already
    # by trying to get it's custom name and description
    display_name = 'Kuma'
    description = 'Student'

    mod_comm = os.path.join(mod_path, unit[1:])
    pa_comm = os.path.join(pa_path, unit[1:])

    # create mod folder if it does not exist
    if not os.path.exists(os.path.dirname(mod_comm)):
        os.makedirs(os.path.dirname(mod_comm))
        
    if os.path.exists(mod_comm):
        comm = json.load(open(mod_comm))
        display_name = comm['display_name']
        description = comm['description']

    if os.path.exists(pa_comm):
        comm = json.load(open(pa_comm))
        comm.pop('tools', None)
        comm['display_name'] = display_name
        comm['description'] = description
        print json.dump(pa_comm, open(), indent=4, sort_keys=True)
