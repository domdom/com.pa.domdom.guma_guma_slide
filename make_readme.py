import os
import json

mode = 'md'

output = ''

unit_list = {
    'kuma' : '/pa/units/commanders/base_commander/base_commander.json',
    'kuma_gun' : '/pa/units/commanders/base_commander/base_commander_bullet_weapon.json',
    'kuma_ammo' : '/pa/units/commanders/base_commander/base_commander_ammo.json',
    'kuma_love_gun' : '/pa/units/commanders/base_commander/love_bullet_weapon.json',
    'kuma_love_ammo' : '/pa/units/commanders/base_commander/love_bullet.json',
    'kuma_build' : '/pa/tools/commander_build_arm/commander_build_arm.json',
    'guma' : '/pa/units/land/assault_bot/assault_bot.json',
    'guma_gun' : '/pa/units/land/assault_bot/assault_bot_tool_weapon.json',
    'guma_ammo' : '/pa/units/land/assault_bot/assault_bot_ammo.json',
    'bot_fac' : '/pa/units/land/bot_factory/bot_factory.json',
    'bot_fac_arm' : '/pa/units/land/bot_factory/bot_factory_build_arm.json',
    'fab_bot' : '/pa/units/land/fabrication_bot_combat/fabrication_bot_combat.json',
    'fab_bot_arm' : '/pa/units/land/fabrication_bot_combat/fabrication_bot_combat_build_arm.json',
    'radar' : '/pa/units/land/radar/radar.json',
    'pgen' : '/pa/units/land/energy_plant/energy_plant.json',
    'mex' : '/pa/units/land/metal_extractor/metal_extractor.json'
}

def load(name):
    f = os.path.join(os.path.abspath('.'), os.path.normpath(name)[1:])
    print(f)
    return json.load(open(f))

def h1(str):
    if mode == 'md': return '# ' + str + '\n'

def h2(str):
    if mode == 'md': return '## ' + str + '\n'

def h3(str):
    if mode == 'md': return '### ' + str + '\n'

def h4(str):
    if mode == 'md': return '#### ' + str + '\n'

def p(str):
    if mode == 'md': return str + '\n\n'

def line(str):
    if mode == 'md': return str + '  \n'

def a(name, link):
    if mode == 'md': return '(%s)[%s]' % (name, link)

output += h1('Guma Guma Slide!')
output += p('A fast paced custom game bringing PA to life with rainbows and beams of love!')

output += h2('What is Guma Guma Slide?')
output += p('''Getting tired of the same old grind in PA? Well have I got a change of pace for you! \
Guma Guma Slide is an exciting, chaotic mod that will have your hands sweating and your heart pumping.\n\n\
Your commander will die in an instant so don't take your eyes off of it for too long. Out micro your opponents \
and lead your horde of Guma to victory. And did I mention the beautiful sparkling rainbow effects? Now you can pwn \
noobs in style with your rainbow bubble and rainbow trail. What more could you want!!?''')

output += h2('Is there lore? Oh yes!')
output += p('''Some time ago, the asteroid Kumaria exploded in the depths of space.

The resulting fragments became a meteor shower that rained down on Earth, and for some reason, bears all over the world rose up and attacked humanity! In "Man vs. Bear", the bears ate the humans and the humans shot the bears, resulting in a seemingly unending battle and a cycle of hatred. In the end, a giant "Wall of Extinction" was erected between the humans and bears and a state of mutual nonaggression came to pass...

Now the Kuma fight to control the essence of yuri love! May your trail shine brightest, and may true love guide you!''')

output += '\n'

def output_guma():
    output = ''

    guma = load(unit_list['guma'])
    guma_gun = load(unit_list['guma_gun'])
    guma_ammo = load(unit_list['guma_ammo'])

    output += h3(guma['display_name'])
    output += p('Fast quick unit, medium range.')

    output += line('Health: ' + str(guma['max_health']))
    output += line('Move Speed: ' + str(guma['navigation']['move_speed']))
    output += line('Sight: ' + str(guma['recon']['observer']['items'][0]['radius']))
    output += p('Metal Cost: ' + str(guma['build_metal_cost']))

    output += line('Rate of fire: ' + str(guma_gun['rate_of_fire']))
    output += line('Range: ' + str(guma_gun['max_range']))
    output += line('Damage: ' + str(guma_ammo['damage']))
    output += line('Splash radius: ' + str(guma_ammo.get('splash_radius', 'None')))
    output += line('(Note: shots move (relatively slowly) at about ' + str(guma_ammo['initial_velocity']) + 'm/s which means how you move your Guma is important)')
    output += p('')

    return output

def output_kuma():
    output = ''

    kuma = load(unit_list['kuma'])
    kuma_gun = load(unit_list['kuma_gun'])
    kuma_ammo = load(unit_list['kuma_ammo'])

    kuma_build = load(unit_list['kuma_build'])

    love_gun = load(unit_list['kuma_love_gun'])
    love_ammo = load(unit_list['kuma_love_ammo'])

    output += h3(kuma['display_name'] + ' (Commander)')
    output += p('Your leader! A fearless Kuma!')

    output += line('Health: ' + str(kuma['max_health']))
    output += line('Move Speed: ' + str(kuma['navigation']['move_speed']))
    output += line('Sight: ' + str(kuma['recon']['observer']['items'][0]['radius']))
    output += p('Metal Cost: ' + str(kuma['build_metal_cost']))

    output += h4('Economy:')
    output += line('  Storage: Metal: ' + str(kuma['storage']['metal']) + ' Energy: ' + str(kuma['storage']['energy']))
    output += line('  Production: Metal: ' + str(kuma['production']['metal']) + ' Energy: ' + str(kuma['production']['energy']))
    output += line('  Build Arm: Metal: ' + str(kuma_build['construction_demand']['metal']) + ' Energy: ' + str(kuma_build['construction_demand']['energy']))
    output += line("  (Commander builds pretty quick! And doesn't use much power)")

    output += h4('Main Weapon:')
    output += line('  Rate of fire: ' + str(kuma_gun['rate_of_fire']))
    output += line('  Range: ' + str(kuma_gun['max_range']))
    output += line('  Damage: ' + str(kuma_ammo['damage']))
    output += line('  Splash damage: ' + str(kuma_ammo.get('splash_damage', 'None')))
    output += line('  Splash radius: ' + str(kuma_ammo.get('splash_radius', 'None')))

    output += h4('Love Gun (commander alt-fire):')
    output += line('  Range: ' + str(love_gun['max_range']))
    output += line('  Damage: ' + str(love_ammo['damage']) + ' (x' + str(love_ammo.get('armor_damage_map', {}).get('AT_Commander', 1)) + ' damage to other Kuma!)')
    output += line('  Splash damage: ' + str(love_ammo.get('splash_damage', 'None')))
    output += line('  Splash radius: ' + str(love_ammo.get('splash_radius', 'None')))
    output += line('  (Huge radius, kill those pesky Guma globs!)')
    output += line('  Can only fire once every ' + str(round(1.0 / love_gun['rate_of_fire'])) + ' seconds. Needs energy to recharge.')
    output += p('')

    return output

def output_honey_flower():
    output = ''

    fab_bot = load(unit_list['fab_bot'])
    fab_bot_arm = load(unit_list['fab_bot_arm'])

    output += h3(fab_bot['display_name'])
    output += p('Slowly repairs nearby buildings and units.')

    output += line('Health: ' + str(fab_bot['max_health']))
    output += line('Move Speed: ' + str(fab_bot['navigation']['move_speed']))
    output += line('Sight: ' + str(fab_bot['recon']['observer']['items'][0]['radius']))
    output += p('Metal Cost: ' + str(fab_bot['build_metal_cost']))

    output += line('Repair Arm: Metal: ' + str(fab_bot_arm['construction_demand']['metal']) + ' Energy: ' + str(fab_bot_arm['construction_demand']['energy']))
    output += p('')

    return output

def output_school():
    output = ''

    bot_fac = load(unit_list['bot_fac'])
    bot_fac_arm = load(unit_list['bot_fac_arm'])

    output += h3(bot_fac['display_name'])
    output += p('Guma training facility! Let your guma spread your True Love Regime!')

    output += line('Health: ' + str(bot_fac['max_health']))
    output += p('Metal Cost: ' + str(bot_fac['build_metal_cost']))

    output += line('Build Arm: Metal: ' + str(bot_fac_arm['construction_demand']['metal']) + ' Energy: ' + str(bot_fac_arm['construction_demand']['energy']))
    output += line('Roll off time: 1 second')
    output += line('(Over time the factory consumes 1 metal and 1 power each second when training guma)')
    output += p('')

    return output

def output_eco():
    output = ''

    pgen = load(unit_list['pgen'])
    mex = load(unit_list['mex'])

    output += h3(pgen['display_name'])
    output += line('Health: ' + str(pgen['max_health']))
    output += line('Metal Cost: ' + str(pgen['build_metal_cost']))
    output += line('Production: Energy: ' + str(pgen['production'].get('energy', 'None')))
    output += p('')


    output += h3(mex['display_name'])
    output += line('Health: ' + str(mex['max_health']))
    output += line('Metal Cost: ' + str(mex['build_metal_cost']))
    output += line('Production: Metal: ' + str(mex['production'].get('metal', 'None')))
    output += p('')

    return output

def output_radar():
    output = ''

    radar = load(unit_list['radar'])

    output += h3(radar['display_name'])
    output += p('Detects frenemy units and buildings!')

    output += line('Health: ' + str(radar['max_health']))
    output += line('Metal Cost: ' + str(radar['build_metal_cost']))
    output += line('Sight Range: ' + str(radar['recon']['observer']['items'][0]['radius']))
    output += line('Radar Range: ' + str(radar['recon']['observer']['items'][1]['radius']))
    output += line('Energy Consumption: None')
    output += line('(The radar still deactivates when there is no power though, so be careful!)')
    output += p('')

    return output

output += h2('Units')
output += output_kuma()
output += output_guma()
output += output_honey_flower()

# output += h3('Economy')
output += h2('Buildings')
output += output_eco()
output += output_school()
output += output_radar()

open('README.md', 'w').write(output)

print(output)
