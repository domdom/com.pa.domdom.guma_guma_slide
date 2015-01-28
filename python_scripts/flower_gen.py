import math
from rainbows import rainbow
# this file is to generate a flower effect
# i've thought about it...this may just require a shit-tonne of particles

points = []

num_points = 50
num_frames = 10

size = 500

segment_length = size / num_points


frame = []
for i in xrange(num_points):
    frame.append([0, i * segment_length])

################
# generate points which look like an opened petal of a lilly
################
# function for making end result petal
# y=sqrt({({1.1})^{2} - ({x - 1})^{2}}) - 0.4x^{3} + 1x - 0.4583
# math.sqrt(1.1**2 - (x - 1)**2) - 0.4 * x ** 3 + x - 0.4583
# y'(x) = -1.2 x^2-x/sqrt(-x^2+2 x+0.21)+1/sqrt(-x^2+2 x+0.21)+1
# -1.2 * x ** 2 - x / math.sqrt(-x ** 2 + 2 * x + 0.21) + 1 / math.sqrt(-x**2 + 2 * x + 0.21) + 1
# function for making start of petal:
# x=({y - 0.5y^{2}})e^{-y}


# generate the angels for the end state

angles_end = []
for i in xrange(num_points - 1):
    a = math.atan2(last_frame[i + 1][1] - last_frame[i][1], last_frame[i + 1][0] - last_frame[i][0])
    x = float((1.3 * i) / num_points)
    angles_end.append(math.atan(-1.2 * x ** 2 - x / math.sqrt(-x ** 2 + 2 * x + 0.21) + 1 / math.sqrt(-x**2 + 2 * x + 0.21) + 1))

segment_length = 4

last_frame = []
x, y = 0, 0
for i in xrange(num_points):
    x = math.sin()
    last_frame.append([x, math.sqrt(1.21 - (x - 1)*(x - 1)) - 0.4 * (x ** 3) + x - 0.4583])



import fileinput
import sys
import re

exp = r'(/\*\s*points\s*\*/)[^/]*(/\*\s*/points\s*\*/)'

for line in fileinput.input('testing_points.html', inplace=True):
    line = re.sub(exp, r'\1 var points = ' + str(points) + r'; \2', line)
    print line,


# y = [row[:] for row in x]


# k is for keyframe

    
    