import json
import pa_paths

mode = 'md'

output = ''

################# constants
"""
"""

unit_list = [
    'pa/units/commanders/base_commander/base_commander.json',
    'pa/units/land/assault_bot/assault_bot.json',
    'pa/units/land/bot_factory/bot_factory.json',
    'pa/units/land/fabrication_bot_combat/fabrication_bot_combat.json',
    'pa/units/land/radar/radar.json',
	'pa/units/land/energy_plant/energy_plant.json',
	'pa/units/land/metal_extractor/metal_extractor.json'
]

def load(name):
    return json.load(open(name))

def h1(str):
    if mode == 'md': return '#' + str + '\n'

def h2(str):
    if mode == 'md': return '##' + str + '\n'

def h3(str):
    if mode == 'md': return '###' + str + '\n'
    
def p(str):
    if mode == 'md': return str + '\n'

def a(name, link):
    if mode == 'md': return '(%s)[%s]' % (name, link)

output += h1('Guma Guma Slide!')
output += p('A fast paced custom game bringing PA to life with rainbows and beams of love!')

open('../readme.md', 'w').write(output)
