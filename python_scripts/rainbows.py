import colorsys

def rainbow(steps, offset=0, revolutions=1, scale=1, time=1):
    r = []
    g = []
    b = []
    
    str = ''
    for i in xrange(steps):
        v = revolutions * float(i) / steps
        
        rgb = colorsys.hsv_to_rgb(v + offset, 1, 1)
        
        r.append([time * float(i)/steps, rgb[0] * scale])
        g.append([time * float(i)/steps, rgb[1] * scale])
        b.append([time * float(i)/steps, rgb[2] * scale])

    str += '{\n'
    str += '"red" : [' + ','.join(['[' + ','.join(["%.2f" % x for x in y]) + ']' for y in r]) + '],\n'
    str += '"green" : [' + ','.join(['[' + ','.join(["%.2f" % x for x in y]) + ']' for y in g]) + '],\n'
    str += '"blue" : [' + ','.join(['[' + ','.join(["%.2f" % x for x in y]) + ']' for y in b]) + ']\n'
    str += '}'
    
    return str
