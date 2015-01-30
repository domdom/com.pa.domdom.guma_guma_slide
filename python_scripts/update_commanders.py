import os
import json

import utils

#root_part = os.path.abspath(os.sep)

print utils.pa_dir()

pa_path = utils.pa_dir()

mod_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

print mod_path

unit_list_path = "/pa/units/unit_list.json"

unit_list = utils.load_base_json(unit_list_path)
unit_list_mod = utils.load_mod_json(unit_list_path)

for unit in unit_list['units']:
    # skip the units which are not commanders
    if '/pa/units/commanders/' not in unit: continue
    # skip avatar commander
    if '/avatar/' in unit: continue
    # make sure we don't overwrite our special base_commander
    if 'base_commander' in unit: continue

    # check if we have that commander already
    # by trying to get it's custom name and description
    display_name = 'Kuma'
    description = 'Student'

    mod_comm = os.path.join(mod_path, unit[1:])
    pa_comm = os.path.join(pa_path, unit[1:])

    if unit not in unit_list_mod['units']:
        print "New commander! ", unit
        unit_list_mod['units'].append(unit)

    # create mod folder if it does not exist
    if not os.path.exists(os.path.dirname(mod_comm)):
        os.makedirs(os.path.dirname(mod_comm))
        
    if os.path.exists(mod_comm):
        comm = utils.load_mod_json(unit)
        display_name = comm['display_name']
        description = comm['description']

    if os.path.exists(pa_comm):
        comm = utils.load_base_json(unit)
        comm.pop('tools', None)
        comm['display_name'] = display_name
        comm['description'] = description
        json.dump(comm, open(mod_comm, 'w'), indent=4)

    # output updated unit_list for the mod
    json.dump(unit_list_mod, open(os.path.join(mod_path, unit_list_path[1:]), 'w'), indent=4)

