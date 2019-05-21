# import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt
from math import sin, cos, pi
import numpy as np

def translate(mat, movement):
    """Translate a matrix in 2-D Cartesian space.

    Uses numpy matrices to translate a collection of 2-Dimensional
    vectors as a geometric translation.

    Positional Arguments:
    mat -- NumPy Matrix that contains all vectors to be translated
    movement -- 2-tuple coordinate to use as the translation.
                Example: Move vectors 2 up and 3 right = (2, 3)
    
    Returns:
    Matrix of translated vectors
    """
    movement = np.array(movement).reshape(2, 1)
    return mat + movement

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

def reflect(mat, point1, point2):
    """Reflect a vector matrix across a line.

    """
    try:
        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
        y_intercept = point1[1] - (slope * point1[0])
    except ZeroDivisionError:
        mat = translate(mat, (-1 * point1[0], 0))
        mat = (np.matrix([[-1, 0],
                          [ 0, 1]]) * mat)
        mat = translate(mat, (point1[0], 0))
        return mat
    if slope == 0:
        mat = translate(mat, (0, -1 * point1[1]))
        mat = (np.matrix([[ 1, 0],
                          [ 0,-1]]) * mat)
        mat = translate(mat, (0, point1[1]))
        return mat
    if y_intercept != 0:
        mat = translate(mat, (0, -1 * y_intercept))
    mat = rotate(mat, (2*pi) - np.arctan(slope), (0, 0))
    mat = (np.matrix([[ 1, 0],
                      [ 0,-1]]) * mat)
    mat = rotate(mat, (2*pi) - np.arctan(slope), (0, 0), counterclock=False)
    if y_intercept != 0:
        mat = translate(mat, (0, y_intercept))
    return mat

def poly_circum_radius(n, s):
    """Calculates the radius of a circle that circumscribes
    a regular polygon with n sides and a sidelength of s.
    """
    radius = s / ((4 - (4 * ((cos(pi / n)) ** 2))) ** 0.5)
    return(radius)

def poly_vertices(n, s, center):
    """Calculates the vertices of a regular polygon with n sides of
    side length s centered at tuple center.
    """
    points = []
    h, k = center
    r = poly_circum_radius(n, s)
    for i in range(n):
        points.append((r * cos(2 * pi / n * i) + h,
                      (r * sin(2 * pi / n * i) + k)))
    return(points)

def sit_straight(vertex_matrix, n, center):
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
    polygon_vertices = poly_vertices(n, s, center)
    if forgraph:
        polygon_vertices.append(polygon_vertices[0])
    vertices_x = [p[0] for p in polygon_vertices]
    vertices_y = [p[1] for p in polygon_vertices]
    vertex_matrix = np.matrix([vertices_x, vertices_y])
    vertex_matrix = sit_straight(vertex_matrix, n, center)
    return(vertex_matrix)

def plotpoly(n, s, center, axes, forgraph, color='k'):
    """Creates and plots a regular polygon on the given axes
    in the given color with the given parameters: n, s, center.
    """
    vertex_matrix = makepoly(n, s, center, forgraph)
    axes.plot([x for x in vertex_matrix[0].flat],
              [y for y in vertex_matrix[1].flat], color)
