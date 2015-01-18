import os
import json
import pa_paths

mode = 'md'

output = ''

################# constants
"""
"""

print pa_paths.get_pa_data_dir()

unit_list = {
    'commander' : '/pa/units/commanders/base_commander/base_commander.json',
    'guma' : '/pa/units/land/assault_bot/assault_bot.json',
    'bot_fac' : '/pa/units/land/bot_factory/bot_factory.json',
    'fab_bot' : '/pa/units/land/fabrication_bot_combat/fabrication_bot_combat.json',
    'radar' : '/pa/units/land/radar/radar.json',
    'pgen' : '/pa/units/land/energy_plant/energy_plant.json',
    'mex' : '/pa/units/land/metal_extractor/metal_extractor.json'
}

def load(name):
    f = os.path.join(os.path.abspath('..'), os.path.normpath(name)[1:])
    print os.path.abspath('..')
    print f
    return json.load(open(f))

def h1(str):
    if mode == 'md': return '#' + str + '\n'

def h2(str):
    if mode == 'md': return '##' + str + '\n'

def h3(str):
    if mode == 'md': return '###' + str + '\n'

def h4(str):
    if mode == 'md': return '####' + str + '\n'
    
def p(str):
    if mode == 'md': return str + '\n'

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

# get unit file for guma!
guma = load(unit_list['guma'])
output += h4(guma['display_name'])
output += p(guma['description'])
output += '\n'

# print json.dumps(guma)

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
Your leader! a fearless Kuma!

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
