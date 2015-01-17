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





open('../readme.md', 'w').write(output)

print output
