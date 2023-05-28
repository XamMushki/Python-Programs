# import numpy as np
from matplotlib import pyplot as plt


def DDA(x1, y1, x2, y2):
    # line drawing algorithm DDA
    # initial point(x1,y1) and end point (x2,y2)

    # calculate dx and dy
    dx = x2-x1
    dy = y2-y1

    # Determine number of steps needed
    steps = 0
    if dx > dy:
        steps = abs(dx)
    else:
        steps = abs(dy)

    # Calculate increment values in x and y directions
    x_inc = dx/steps
    y_inc = dy/steps

    x_coordinates = []
    y_coordinates = []

    # Start drawing
    x, y = x1, y1
    while steps:
        # in case of actual drawing we need the rounded values,
        # because coordinates of a pixels will always be integers.
        # x_coordinates.append(round(x))
        # y_coordinates.append(round(y))

        x_coordinates.append(x)
        y_coordinates.append(y)

        x += x_inc
        y += y_inc

        steps -= 1

    plt.plot(x_coordinates, y_coordinates)
    plt.show()


if __name__ == '__main__':
    # initial point(2,2) and end point(6,12)
    DDA(2, 2, 6, 12)
