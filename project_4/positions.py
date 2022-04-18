# rendom.random() draws random values between 0.0 and 1.0
from random import random
# random.uniform() draws random values from specified set (eg. between -1.0 and 1.0)
from random import uniform

import numpy as np

def randomPositions(howMany):
    '''Generates random positions in Cartesian system\n
        howMany = int number of how many coordinates we want to generate'''
    x = []*howMany
    y = []*howMany

    i = 0

    # this loop draws two random values and appends them to lists of coordinates
    for i in range(i, howMany):
        x.append(uniform(-1, 1))
        y.append(uniform(-1, 1))

    return x, y


def randomPositionsPolar(howMany):
    '''Generates random positions in polar coordinates and projects them onto Cartesian system\n
        howMany = int number of how many coordinates we want to generate'''

    radius = []*howMany
    angle = []*howMany
    x = []*howMany
    y = []*howMany

    i = 0

    # this loop draws two random values and appends them to lsit of radiuses and angles
    for i in range(i, howMany):
        radius.append(random())
        angle.append(random()*2*np.pi)

    # loop which projects polar coordinates to cartesian
    for i in range(0, howMany):
        x.append(radius[i]*np.cos(angle[i]))
        y.append(radius[i]*np.sin(angle[i]))

    return x, y


if __name__ == "__main__":

    # randomPositions(number) generates (number) of coordinates, each between -1 and 1
    x, y = randomPositions(5)
    for i in range(0, 5):
        assert -1 <= x[i] <= 1
        assert -1 <= y[i] <= 1

    # randomPositions(number) generates (number) of coordinates, each between -1 and 1
    x2, y2 = randomPositionsPolar(5)
    for i in range(0, 5):
        assert -1 < x2[i] < 1
        assert -1 < y2[i] < 1
