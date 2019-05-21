import sys
import geomlib as glib
import matplotlib.pyplot as plt
import numpy as np
from math import pi

def polygonpics(file_prefix=''):
    """Generates polygons from n = 3-30.

    Arguments:
    file_prefix - string to prepend to the saved file to change directory
    """
    for i in range(3, 10):
        n = i
        s = 3
        center = (0, 0)
        forgraph = True
        fig, axes= plt.subplots()
        glib.plotpoly(n, s, center, axes, True, 'b')
        axes.set_aspect('equal')
        axes.set_xticks([])
        axes.set_yticks([])
        axes.spines['right'].set_color('none')
        axes.spines['bottom'].set_color('none')
        axes.spines['left'].set_color('none')
        axes.spines['top'].set_color('none')
        axes.set_title('{}-gon'.format(i))
        fig.savefig(file_prefix + '{:04d}-gon.svg'.format(i))
        plt.close('all')

def rotations(file_prefix=''):
    """Plots a polygon, rotates it a little bit, plots it again,
    and continues all the way around the circle. Repeats for
    n = 3 - 6.

    Arguments:
    file_prefix - string to prepend to the saved file to change directory
    """
    for i in range(3, 7):
        n = i
        s = 3
        center = (0, 0)
        forgraph = True
        rotations = np.linspace(0, 2 * pi, 100, endpoint=False)
        fig, axes = plt.subplots()
        for j in range(len(rotations)):
            vertex_matrix = glib.makepoly(n, s, center, forgraph)
            vertex_matrix = glib.rotate(vertex_matrix, rotations[j],
                                      center, counterclock=False)
            axes.plot([x for x in vertex_matrix[0].flat],
                      [y for y in vertex_matrix[1].flat], 'r', lw='0.05')
        axes.set_aspect('equal')
        axes.set_xticks([])
        axes.set_yticks([])
        axes.spines['right'].set_color('none')
        axes.spines['bottom'].set_color('none')
        axes.spines['left'].set_color('none')
        axes.spines['top'].set_color('none')
        axes.set_title('{}-gon'.format(i))
        fig.savefig(file_prefix + '{:04d}-gon_rotated.svg'.format(i))
        plt.close('all')

def colorconcentrics(file_prefix=''):
    """Plots a polygon, increases the size exponentially, cycles to
    a new color, and plot again. Repeat many times.

    Arguments:
    file_prefix - string to prepend to the saved file to change directory
    """
    colors = []
    for i in range(20):
        colors += ['b', 'g', 'r']
    sides = range(1, len(colors) + 1, 1)
    for i in range(3, 9):
        n = i
        center = (0, 0)
        forgraph = True
        fig, axes = plt.subplots()
        for j in range(len(sides)):
            s = sides[j] ** 2
            glib.plotpoly(n, s, center, axes, forgraph, colors[j])
        axes.set_aspect('equal')
        axes.set_xticks([])
        axes.set_yticks([])
        axes.spines['right'].set_color('none')
        axes.spines['bottom'].set_color('none')
        axes.spines['left'].set_color('none')
        axes.spines['top'].set_color('none')
        fig.savefig(file_prefix + '{:04d}-gon_colorconc.svg'.format(i))
        plt.close('all')

def main():
    fp = input('Enter a relative path to save the files under (Ex: "temp/"):\n')
    polygonpics(file_prefix=fp)
    rotations(file_prefix=fp)
    colorconcentrics(file_prefix=fp)

if __name__ == '__main__':
    main()
