import math

l = 0.1

r = 5

c = 20

for dt in [0.0, 0.33, 0.66]:
    x = []
    z = []
    xv = []
    zv = []
        
    for i in xrange(c + 1):
        t = float(i) / float(c) + dt
        x.append([t - dt, r * math.sin(math.pi * 2 * t)])
        z.append([t - dt, r * math.cos(math.pi * 2 * t)])
        xv.append([t - dt, -r * math.sin(math.pi * 2 * t) / l])
        zv.append([t - dt, -r * math.cos(math.pi * 2 * t) / l])

    print '      "velocityX" : ' + str(xv) + ','
    print '      "velocityZ" : ' + str(zv) + ','

    print '      "offsetX" : ' + str(x) + ','
    print '      "offsetZ" : ' + str(z) + ','

    print ''
