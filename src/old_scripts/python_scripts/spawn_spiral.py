import math
# Used for making rainbows
import colorsys
import utils

import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.5g')
import collections
import copy

base_landing_spec_path = 'rainbow_commander_landing.pfx'
gen_landing_spec_path = 'gen_rainbow_commander_landing.pfx'

base = utils.load_local_json(base_landing_spec_path)

time = 0

def clear_all():
    base['emitters'] = []

def add_spirals():
    base_spiral = json.loads('''{
        "spec" : {
            "shader": "particle_add",
            "shape": "rectangle",
            "baseTexture": "/pa/effects/textures/particles/softdot.papa",
            "rampTexture": "/pa/effects/textures/particles/uncompressed/flicker_ramp.papa",
            "facing": "velocity",
            "size": [[0, 0], [0.1, 1], [1, 0]],
            "alpha": [[0, 0], [0.1, 6], [1, 0]]
        },
        "useWorldSpace" : true,
        "lifetime": 2,
        "emitterLifetime": 5,
        "emissionRate" : [[0, 50], [5, 100]],
        "bLoop": false,
        "delay": 2,
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
    secondary_thickness = 1.5

    primary_v = 10
    secondary_v = 9

    primary_drag = math.pow(0.5, 1.0/60.0)

    global time
    time = base_spiral['emitterLifetime']
    time_steps = (time * 50)

    # this function converts a time into a radius for offset
    def r(t):
        return 2.0

    def twist(t):
        return (1 - math.cos(t / time * math.pi)) * 5


    # make the spirals
    for i in xrange(primary_num * 3):
        emitter = copy.deepcopy(base_spiral)

        offset = (float(i) / primary_num) / 3.0

        rgb = colorsys.hsv_to_rgb(math.fmod(offset + 1.0/12, 1), 1, 1)
        rgb = rgb[0] * 4, rgb[1] * 4, rgb[2] * 4
        
        emitter['spec']['red'], emitter['spec']['green'], emitter['spec']['blue'] = rgb

        emitter['sizeX'] = secondary_thickness if i % 3 else primary_thickness

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
            a = (float(j) / time_steps) * math.pi * 2 * twist(t) + (offset * math.pi * 2)
            emitter['offsetX'].append([t, math.cos(a) * r(t)])
            emitter['offsetY'].append([t, math.sin(a) * r(t)])
            emitter['offsetZ'].append([t, 900 - t * 300])

            emitter['velocityX'].append([t, math.cos(a)])
            emitter['velocityY'].append([t, math.sin(a)])



            emitter['velocity'].append([t, 70 - t / time * 60])

        # add each emitter to the effects
        base['emitters'].append(emitter)

def add_rings():
    base_ring = json.loads('''    {
          "spec": {
            "shader": "particle_add",
            "facing": "velocity",
            "size": [[0, 1], [1, 0]],
            "red": 1,
            "green": 1,
            "blue": 1,
            "alpha": [[0, 0], [0.05, 0], [0.051, 5]],
            "baseTexture": "/pa/effects/textures/particles/flat.papa",
            "dataChannelFormat": "PositionAndColor"
          },
          "offsetX": 0,
          "offsetY": 0,
          "offsetZ": 0,
          "offsetRangeX": 0,
          "offsetRangeY": 0,
          "offsetRangeZ": 0,
          "velocityRangeX": 1,
          "velocityRangeY": 1,
          "velocityRangeZ": 0,
          "velocity": 150,
          "velocityRange": 1,
          "drag": 0.9887,
          "dragRange": 0.01,
          "sizeX": 4,
          "sizeRangeX": 1,
          "offsetZ": [[0, 900], [3, 0]],
          "delay": 2,
          "lifetime": 2,
          "emitterLifetime": 3,
          "bLoop": false,
          "endDistance": -1
        }''', object_pairs_hook=collections.OrderedDict)



    num_rings = 10

    base_ring['emissionBursts'] = []

    # lets make some rings!
    for i in xrange(num_rings):
        base_ring['emissionBursts'].append({"time": float(i) / num_rings * time, "count": 150, "countRange": 0})

    # add ring effect 
    base['emitters'].append(base_ring)


add_spirals()
add_rings()

json.dump(base, open(gen_landing_spec_path, 'w'), separators=(',',':'))

        
        
    

    
    
    
    
    
