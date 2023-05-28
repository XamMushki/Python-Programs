from matplotlib import pyplot as plt
import numpy as np


def midpointCircleAlg(r, x1=0):
    # Uses the concept of 8-way symmetry
    # Plot the eight symmetric points
    # (x, y), (-x, y), (x, -y), (-x, -y), (y, x), (-y, x), (y, -x), (-y, -x)
    # on the circle using the center coordinates (xc, yc).
    # initial point(x1,r), where we assume that x1=0
    x_coordinates = [x1]
    y_coordinates = [r]

    # find initial decision parameter
    d = 1-r

    x, y = x1, r
    while x <= y:
        if d < 0:
            x = x+1
            x_coordinates.append(x)
            y_coordinates.append(y)
            d = d+(2*x)+3
        elif d >= 0:
            x = x+1
            y = y-1
            x_coordinates.append(x)
            y_coordinates.append(y)
            d = d+(2*(x-y))+5

    x_coordinates = np.array(x_coordinates)
    y_coordinates = np.array(y_coordinates)
    # Plotting (x,y)
    plt.plot(x_coordinates, y_coordinates)
    # Plotting (-x,y)
    plt.plot(x_coordinates*-1, y_coordinates)
    # Plotting (x,-y)
    plt.plot(x_coordinates, y_coordinates*-1)
    # Plotting (-x,-y)
    plt.plot(x_coordinates*-1, y_coordinates*-1)
    # Plotting (y, x)
    plt.plot(y_coordinates, x_coordinates)
    # Plotting  (-y, x)
    plt.plot(y_coordinates*-1, x_coordinates)
    # Plotting (y, -x)
    plt.plot(y_coordinates, x_coordinates*-1)
    # Plotting (-y, -x)
    plt.plot(y_coordinates*-1, x_coordinates*-1)
    plt.suptitle('MidPoint Circle Drawing Algorithm')
    # plt.savefig('circle')
    plt.show()


if __name__ == '__main__':
    radius = 500
    midpointCircleAlg(radius)
