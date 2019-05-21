"""
def translate(mat, movement):
def rotate(mat, theta, center, counterclock=True):
def reflect(mat, point1, point2):
"""

import geomlib as gl
import numpy as np

a = np.matrix([[2, 3, 6],
               [7, 1, 4]])
b = np.matrix([[1, 1, 5],
               [0, 3, 0]])
c = np.matrix([[4, 4, 2],
               [-1, -4, -4]])

print('TEST 1: TRANSLATE')
print('=================')
print('a =')
print(a)
print()

print('Translate: [4.75, -2.0]')
print('=======================')
print('Translated a =')
print(gl.translate(a, (4.75, -2.0)))
print()

print('Translate: [0, 0]')
print('=================')
print('Translated a =')
print(gl.translate(a, (0, 0)))
print()

print()
print('-'*100)
print()

print('TEST 2: ROTATE')
print('==============')
print('b =')
print(b)
print()

print('Rotate: theta        = 0')
print('        center       = (0, 0)')
print('        counterclock = True')
print('============================')
print('ANSWER =')
rot_b = b
print(rot_b)
print('Rotated b =')
print(gl.rotate(b, 0, (0, 0)))
print()

print('Rotate: theta        = π')
print('        center       = (0, 0)')
print('        counterclock = True')
print('=============================')
print('ANSWER =')
rot_b = np.matrix([[-1, -1, -5],
                   [0, -3, 0]])
print(rot_b)
print('Rotated b =')
print(gl.rotate(b, np.pi, (0, 0)))
print()

print('Rotate: theta        = π')
print('        center       = (-2, -1)')
print('        counterclock = True')
print('===============================')
print('ANSWER =')
rot_b = np.matrix([[-5, -5, -9],
                   [-2, -5, -2]])
print(rot_b)
print('Rotated b =')
print(gl.rotate(b, np.pi, (-2, -1)))
print()

print('Rotate: theta        = π')
print('        center       = (-2, -1)')
print('        counterclock = False')
print('===============================')
print('ANSWER =')
rot_b = np.matrix([[-5, -5, -9],
                   [-2, -5, -2]])
print(rot_b)
print('Rotated b =')
print(gl.rotate(b, np.pi, (-2, -1)))
print()

print('Rotate: theta        = π/4')
print('        center       = (-1, -2)')
print('        counterclock = True')
print('===============================')
print('ANSWER =')
rot_b = np.matrix([[-1, -3.1213, 1.8284],
                   [0.8284, 2.9497, 3.6568]])
print(rot_b)
print('Rotated b =')
print(gl.rotate(b, np.pi/4, (-1, -2)))
print()

print()
print('-'*100)
print()

print('TEST 3: REFLECT')
print('===============')
print('c =')
print(c)
print()

print('Reflect: point1 = (0, 0)')
print('         point2 = (1, 0)')
print('         X-Axis')
print('========================')
print('ANSWER =')
refl_c = np.matrix([[4, 4, 2],
                    [1, 4, 4]])
print(refl_c)
print('Reflected c =')
print(gl.reflect(c, (0,0), (1,0)))
print()

print('Reflect: point1 = (0, 0)')
print('         point2 = (0, 1)')
print('         Y-Axis')
print('========================')
print('ANSWER =')
refl_c = np.matrix([[-4, -4, -2],
                    [-1, -4, -4]])
print(refl_c)
print('Reflected c =')
print(gl.reflect(c, (0,0), (0,1)))
print()

print('Reflect: point1 = (0, 2)')
print('         point2 = (1, 2)')
print('         Horizontal Line')
print('========================')
print('ANSWER =')
refl_c = np.matrix([[4, 4, 2],
                    [5, 8, 8]])
print(refl_c)
print('Reflected c =')
print(gl.reflect(c, (0,2), (1,2)))
print()

print('Reflect: point1 = (6, 0)')
print('         point2 = (6, 1)')
print('         Vertical Line')
print('========================')
print('ANSWER =')
refl_c = np.matrix([[8, 8, 10],
                    [-1, -4, -4]])
print(refl_c)
print('Reflected c =')
print(gl.reflect(c, (6,0), (6,1)))
print()

print('Reflect: point1 = (0, -2)')
print('         point2 = (2, 0)')
print('========================')
print('ANSWER =')
refl_c = np.matrix([[1, -2, -2],
                    [2, 2, 0]])
print(refl_c)
print('Reflected c =')
print(gl.reflect(c, (0,-2), (2,0)))
print()
