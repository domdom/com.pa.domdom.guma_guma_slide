import math
# Used for making rainbows
import rainbows
import utils

import json
import collections
import copy

base_landing_spec_path = 'rainbow_commander_landing.pfx'
gen_landing_spec_path = 'gen_rainbow_commander_landing.pfx'

base_spiral = json.loads('''{
    "spec" : {
        "shader": "particle_transparent",
        "shape": "string",
        "size": [[0, 0], [0.1, 1], [1, 0]],
        "alpha": [[0, 0], [0.1, 1], [1, 0]],
        "baseTexture": "/pa/effects/textures/particles/flat.papa",
        "rampTexture": "/pa/effects/textures/particles/uncompressed/no_ramp.papa"
    },
    "useWorldSpace" : true,
    "lifetime": 2,
    "emitterLifetime": 5,
    "emissionRate" : 100,
    "bLoop": false,
    "delay": 5,
    "endDistance": -1
}''', object_pairs_hook=collections.OrderedDict)

##### My plan
# generate 6 spirals in total, 3 primary ones which are slightly thicker
# and 3 secondary ones which are a little thinner
# each spiral will be a separate color

# simultaneously generate some sparkle effects, that appear slightly later than the spirals

# parameters for our generating the effects
primary_thickness = 4
primary_num = 3
secondary_thickness = 1

primary_v = 10
secondary_v = 9

primary_drag = math.pow(0.5, 1.0/60.0)

time = base_spiral['emitterLifetime']
time_steps = time * base_spiral['emissionRate']

base = utils.load_local_json(base_landing_spec_path)

# this function converts a time into a radius for offset
def r(t):
    return 2.0


base['emitters'] = []

for i in xrange(primary_num * 2):
    emitter = copy.deepcopy(base_spiral)

    offset = (float(i) / primary_num) / 2.0
    
    # choose a color for this spiral
    rgb = rainbows.rgb_from_hsv(math.fmod(offset + 1.0/12, 1))
    rgb = rgb[0] * 4, rgb[1] * 4, rgb[2] * 4
    
    emitter['spec']['red'], emitter['spec']['green'], emitter['spec']['blue'] = rgb

    emitter['size'] = 4
    emitter['delay'] = 3

    # set the offsets as an array
    emitter['offsetX'] = []
    emitter['offsetY'] = []
    emitter['offsetZ'] = []


    emitter['velocityX'] = []
    emitter['velocityY'] = []
    emitter['velocityZ'] = 0

    emitter['velocity'] = []
    

    for j in xrange(time_steps):
        t = (float(j) / time_steps) * time
        # angle (convert time into rotations 3 at the end means each spiral goes around 3 times)
        a = (float(j) / time_steps) * math.pi * 2 * 3 + (offset * math.pi * 2)
        emitter['offsetX'].append([t, math.cos(a) * r(t)])
        emitter['offsetY'].append([t, math.sin(a) * r(t)])
        emitter['offsetZ'].append([t, 900 - t * 300])

        emitter['velocityX'].append([t, math.cos(a)])
        emitter['velocityY'].append([t, math.sin(a)])


        emitter['velocity'] = 30

    base['emitters'].append(emitter)
    

json.dump(base, open(gen_landing_spec_path, 'w'))

        
        
    

    
    
    
    
    
