"""
* AUTHOR : Prathamesh Tibile
* Date   : 28-07-21
* Time   : 9.00 PM
* Title  : Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
"""
import math

class Point:
    pass

first = Point()
second = Point()

first.x1 = float(input('Enter the x1 co-ordinate of the first point:'))
first.y1 = float(input('Enter the y1 co-ordinate of the first point:'))

second.x2 = float(input('Enter the x2 co-ordinate of the second point:'))
second.y2 = float(input('Enter the y2 co-ordinate of the second point:'))


def dist(original, final):
    dist = math.sqrt((original.x1 - final.x2) * (original.x1 - final.x2) + (original.y1 - final.y2) * (original.y1 - final.y2))
    return dist


dist = dist(first, second)

print('Distance Between two Points :', dist)