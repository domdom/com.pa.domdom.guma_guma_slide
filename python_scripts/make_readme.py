import os
import json
import utils

from collections import OrderedDict

mode = 'md'

output = ''

################# constants
"""
"""

print utils.pa_dir()

unit_list = OrderedDict([
    ('commander', '/pa/units/commanders/base_commander/base_commander.json'),
    ('guma', '/pa/units/land/assault_bot/assault_bot.json'),
    ('fab_bot', '/pa/units/land/fabrication_bot_combat/fabrication_bot_combat.json'),
    ('bot_fac', '/pa/units/land/bot_factory/bot_factory.json'),
    ('radar', '/pa/units/land/radar/radar.json'),
    ('pgen', '/pa/units/land/energy_plant/energy_plant.json'),
    ('mex', '/pa/units/land/metal_extractor/metal_extractor.json')
])

def load(name):
	return utils.load_mod_json(name)

def join(arg, glue=''):
	return glue.join([str(x) for x in arg])

def h1(*arg):
    if mode == 'md': return '#' + join(arg) + '\n'

def h2(*arg):
    if mode == 'md': return '##' + join(arg) + '\n'

def h3(*arg):
    if mode == 'md': return '###' + join(arg) + '\n'

def h4(*arg):
    if mode == 'md': return '####' + join(arg) + '\n'

def h5(*arg):
    if mode == 'md': return '#####' + join(arg) + '\n'
    
def p(*arg):
    if mode == 'md': return join(arg) + '\n'

def a(name, link):
    if mode == 'md': return '(%s)[%s]' % (name, link)

output += h1('Guma Guma Slide!')
output += p('A fast paced custom game bringing PA to life with rainbows and beams of love!')

output += h2('What is Guma Guma Slide?')
output += p('Getting tired of the same old grind in PA? Well have I got a change of pace for you! \
Guma Guma Slide is an exciting, chaotic mod that will have your hands sweating and your heart pumping.\n\n\
Your commander will die in an instant so don\'t take your eyes off of it for too long. Out micro your opponents \
and lead your horde of Guma to victory. And did I mention the beautiful sparkling rainbow effects? Now you can pwn \
noobs in style with your rainbow bubble and rainbow trail. What more could you want!!?')

output += h2('Is there lore? Oh yes!')
output += p('''Some time ago, the asteroid Kumaria exploded in the depths of space.

The resulting fragments became a meteor shower that rained down on Earth, and for some reason, bears all over the world rose up and attacked humanity! In "Man vs. Bear", the bears ate the humans and the humans shot the bears, resulting in a seemingly unending battle and a cycle of hatred. In the end, a giant "Wall of Extinction" was erected between the humans and bears and a state of mutual nonaggression came to pass...

Now the Kuma fight to control the essence of yuri love! May your trail shine brightest, and may true love guide you!''')

output += h2('Mod Details')
output += h3('Guma Guma Slide Units')

output += '\n'

def print_unit(name):
	output = ''
	# get unit file for guma!
	unit = load(unit_list[name])
	output += h4(unit['display_name'])
	output += p(unit['description'])
	output += '\n'
	output += p('Health: ' + str(unit['max_health']) + ', Metal Cost: ' + str(unit['build_metal_cost']))

	output += h5('General')
	if 'command_caps' in unit:
		output += p('Commands: ', join([x.replace('ORDER_', '') for x in unit['command_caps']], ', '), '  ')
	if 'navigation' in unit:
		output += p('Speed: ', unit['navigation']['move_speed'], ' m/s, Accel: ', unit['navigation']['acceleration'],\
		' m/s/s, Brake: ', unit['navigation']['brake'], ' m/s/s, Turn: ', unit['navigation']['turn_speed'], ' degrees/s  ')
	output += '\n'
	if 'command_caps' in unit and 'ORDER_Attack' in unit['command_caps']:
		output += h5('Attack')


	return output

for unit in unit_list:
	output += print_unit(unit)

'''
Guma:
Fast quick unit, medium range.

Health: 1
Move Speed: 45
Sight: 150
Metal Cost: 3

Rate of fire: 3 attacks per second
Range: 75
Damage: 3
Splash: None
(Note: shots move at about 60m/s which means how you move your Guma is important)

Honey Flower:
Slow healing unit, no attack.

Health: 100
Move speed: 5
Sight: 100
Metal Cost: 30

Build Arm: Metal: 2 Energy: 0

Kuma (Commander):
Your leader! A fearless Kuma!

Health: 1200
Move speed: 45
Sight: 200
Metal cost: 120

Rate of fire: 1 attack per second
Range: 100
Damage: 2
Splash Damage: 1
Splash Radius: 2
(Is auto attack)

Kuma's Kannon!
Ammo: Energy
Ammo limit: 1 shot
Ammo demand: 0.03 energy per second
Energy needed per shot: 1
Cooldown: 33 Seconds

Damage: 1
Splash damage: 1
Splash Radius Full Damage: 40
(Huge radius, kill those pesky Guma globs!)

Kuma's Economy:
Production: Energy: 2, Metal: 4
Storage: Energy: 15, Metal: 50

Build Arm: Metal: 4, Energy: 1
(Commander builds pretty quick! and doesn't use much power)


General Economy of Guma Guma Slide:
Energy Plant:
Health: 200
Metal Cost: 30
Production: Energy: 1

Metal Extractor:
Health: 100
Metal Cost: 10
Production: Metal: 1

Other Guma Guma Buildings!
Guma Factory:
Health: 1000
Metal Cost: 40
Build Arm: Energy: 1.5, Metal: 1.5
Roll off time: 1 Second
(Over time the factory consumes 1 metal and 1 power each second)

Radar:
Health: 500
Metal Cost: 12
Sight Range: 100
Radar Range: 600
Energy Consumption: None
(The radar still deactivates when there is no power though, so be careful!)


FUTURE PLANS:
In the future we are going to be adding:
Unit Icons,
Unit Textures,
Balance Changes, (Any feedback on balance is very appreciated)

Our Mission:
To create something fun and fast paced.

'''


open('../readme.md', 'w').write(output)

print output
