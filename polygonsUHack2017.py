# import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt
from math import sin, cos, pi
import numpy as np
import os

def rotate(mat, theta, center, counterclock=True):
    """Rotate a vector matrix around a point.

    Uses numpy matrices to rotate a collection of 2-Dimensional
    vectors as a geometric transformation.

    Positional Arguments:
    mat -- NumPy Matrix that contains all vectors to be rotated
    theta -- float angle in radians to rotate the vector matrix
    center -- 2-tuple coordinate to use as center of rotation

    Optional Arguments:
    counterclock -- boolean; rotates counterclockwise if True
                             clockwise if False

    Returns:
    Matrix of rotated vectors
    """
    if center == (0, 0):
        if counterclock:
            rotmat = np.matrix([[cos(theta), cos(theta + (pi / 2))],
                                [sin(theta), sin(theta + (pi / 2))]])
        else:
            rotmat = np.matrix([[cos(-1*theta), cos((-1*theta) + (pi / 2))],
                                [sin(-1*theta), sin((-1*theta) + (pi / 2))]])
        return(rotmat * mat)
    else:
        if counterclock:
            return(translate(
                       rotate(
                           translate(mat, (-1 * center[0], -1 * center[1])),
                           theta, (0, 0)),
                       center))
        else:
            return(translate(
                       rotate(
                           translate(mat, (-1 * center[0], -1 * center[1])),
                           theta, (0, 0), counterclock=False),
                       center))

def polycircumradius(n, s):
    """Calculates the radius of a circle that circumscribes
    a regular polygon with n sides and a sidelength of s.
    """
    radius = s / ((4 - (4 * ((cos(pi / n)) ** 2))) ** 0.5)
    return(radius)

def vertices(n, s, center):
    """Calculates the vertices of a regular polygon with n sides of
    side length s centered at tuple center.
    """
    points = []
    h, k = center
    r = polycircumradius(n, s)
    for i in range(n):
        points.append((r * cos(2 * pi / n * i) + h,
                      (r * sin(2 * pi / n * i) + k)))
    return(points)

def sitstraight(vertex_matrix, n, center):
    """Rotates a regular polygon the correct amount to make it
    sit "flat on a side".
    """
    if n % 2 == 1:
        vertex_matrix = rotate(vertex_matrix, (pi / 2) - ((pi * (n - 2)) / n),
                                  center, counterclock=False)
    elif n % 4 == 0:
        vertex_matrix = rotate(vertex_matrix,
                                  (pi / 2) - ((pi * (n - 2)) / (2 * n)),
                                  center, counterclock=False)
    return(vertex_matrix)

def makepoly(n, s, center, forgraph):
    """Creates a regular polygon of n sides of side length s
    at tuple center. If forgraph is true, the final point is the
    same as the beginning point (so that a plotting function
    completes the shape).
    """
    polygon_vertices = vertices(n, s, center)
    if forgraph:
        polygon_vertices.append(polygon_vertices[0])
    vertices_x = [p[0] for p in polygon_vertices]
    vertices_y = [p[1] for p in polygon_vertices]
    vertex_matrix = np.matrix([vertices_x, vertices_y])
    vertex_matrix = sitstraight(vertex_matrix, n, center)
    return(vertex_matrix)

def plotpoly(n, s, center, axes, forgraph, color='k'):
    """Creates and plots a regular polygon on the given axes
    in the given color with the given parameters: n, s, center.
    """
    vertex_matrix = makepoly(n, s, center, forgraph)
    axes.plot([x for x in vertex_matrix[0].flat],
              [y for y in vertex_matrix[1].flat], color)


######################
#    Demo Methods    #
######################

def polygonpics():
    """Generates polygons from n = 3-30.
    """
    for i in range(3, 31):
        n = i
        s = 3
        center = (0, 0)
        forgraph = True
        fig, axes= plt.subplots()
        plotpoly(n, s, center, axes, True, 'b')
        axes.set_aspect('equal')
        axes.set_xticks([])
        axes.set_yticks([])
        axes.spines['right'].set_color('none')
        axes.spines['bottom'].set_color('none')
        axes.spines['left'].set_color('none')
        axes.spines['top'].set_color('none')
        axes.set_title('{}-gon'.format(i))
        fig.savefig('{:04d}-gon.pdf'.format(i))
        plt.close('all')

def rotations():
    """Plots a polygon, rotates it a little bit, plots it again,
    and continues all the way around the circle. Repeats for
    n = 3 - 6.
    """
    for i in range(3, 7):
        n = i
        s = 3
        center = (0, 0)
        forgraph = True
        rotations = np.linspace(0, 2 * pi, 100)
        fig, axes = plt.subplots()
        for j in range(len(rotations)):
            vertex_matrix = makepoly(n, s, center, forgraph)
            vertex_matrix = rotate(vertex_matrix, rotations[j],
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
        fig.savefig('{:04d}-gon_rotated.pdf'.format(i))
        plt.close('all')

def colorconcentrics():
    """Plots a polygon, increases the size exponentially, cycles to
    a new color, and plot again. Repeat many times.
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
            plotpoly(n, s, center, axes, forgraph, colors[j])
        axes.set_aspect('equal')
        axes.set_xticks([])
        axes.set_yticks([])
        axes.spines['right'].set_color('none')
        axes.spines['bottom'].set_color('none')
        axes.spines['left'].set_color('none')
        axes.spines['top'].set_color('none')
        fig.savefig('{:04d}-gon_colorconc.pdf'.format(i))
        plt.close('all')

polygonpics()
rotations()
colorconcentrics()
