import colorsys

lifetime = 3

c = 40
revs = 3
scale = 10
time = 1

for dt in [0.0, 0.33, 0.5]:
    r = []
    g = []
    b = []
    for i in xrange(c+1):
        v = revs * float(i) / c
        
        rgb = colorsys.hsv_to_rgb(v + dt, 1, 1)
        
        r.append([time * float(i)/c, rgb[0] * scale])
        g.append([time * float(i)/c, rgb[1] * scale])
        b.append([time * float(i)/c, rgb[2] * scale + 20])

    print '"red" : [' + ','.join(['[' + ','.join(["%.2f" % x for x in y]) + ']' for y in r]) + '],'
    print '"green" : [' + ','.join(['[' + ','.join(["%.2f" % x for x in y]) + ']' for y in g]) + '],'
    print '"blue" : [' + ','.join(['[' + ','.join(["%.2f" % x for x in y]) + ']' for y in b]) + '],'
    print ''
