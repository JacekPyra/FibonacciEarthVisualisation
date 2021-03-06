# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
im = img.imread('HuffmanPatterson.png')


def longitude_degrees(x, y):
    t = np.arctan2(y, x)
    t += 3.14159265
    return t


def latitude_degrees(r, z):
    t = np.arctan2(z, r)
    return t


def set_color(x, y, z, radius):
    longitude = longitude_degrees(x, y)
    latitude = latitude_degrees((radius**.38), z)
    x = 334 * longitude

    pi = np.pi
    y = (np.log(np.tan(pi / 4 + latitude / 2))) * 330 + 525
    if abs(y) > 1049:
        y = 0
    else:
        y = -y
    return im[int(y), int(x), :][1]


def fibonacci_sphere(samples=100):
    # https://stackoverflow.com/a/26127012

    x_array = []
    y_array = []
    z_array = []
    color = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians
    z_samples = np.linspace(1 / samples - 1, 1 - 1 / samples, samples)

    for i, z in enumerate(z_samples):
        # y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1

        radius = math.sqrt(1 - z * z)  # radius at y
        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        y = math.sin(theta) * radius

        x_array.append(x)
        y_array.append(y)
        z_array.append(z)
        color.append(set_color(x, y, z, radius))
    return x_array, y_array, z_array, color


def plot_distribution(samples, x, y, z):
    t = np.arange(-1, 1, 1/samples*2)
    # red dashes, blue squares and green triangles
    plt.plot(t, x, 'r--', t, y, 'bs', t, z, 'g^')
    plt.show()


def main():
    xa, ya, za, col = fibonacci_sphere(100000)
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter(xa, ya, za, c=col)
    ax.legend("kc")
    plt.show()


if __name__ == '__main__':
    main()
