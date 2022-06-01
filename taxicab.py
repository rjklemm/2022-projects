"""
Bob Klemm
5/27/2022

'Taxicab Distance'
"""

from ast import Return
import math

#2D taxicab distance
#inputs are two 1x2 vectors with point coordinates
def distance2(point1, point2):
    if len(point1) == len(point2):
        xdiff = point2[0] - point1[0]
        ydiff = point2[1] - point1[1]
        distance = xdiff + ydiff
        return distance
    else:
        print('Points do not have the same number of dimensions.')
        

#example of using 2D distnace function
dist = distance2([0,0],[3,4])
print(dist)


#3D taxicab distance
#inputs are two 1x3 vectors with point coordinates
def distance3(point1, point2):
    if len(point1) == len(point2):
        xdiff = point2[0] - point1[0]
        ydiff = point2[1] - point1[1]
        zdiff = point2[2] - point1[2]
        distance = xdiff + ydiff + zdiff
        return distance
    else:
        print('Points do not have the same number of dimensions.')
        

#example of using 3D distance function
dist = distance3([0,0,0],[3,4,5])
print(dist)


#N-dimesional taxicab distance
#inputs are two 1xN vectors with point coordinates
def distanceN(point1, point2):
    if len(point1) == len(point2):
        sum = 0
        for i in range(0,len(point1)):
            diff = point2[i] - point1[i]
            sum += diff
            distance = sum
        return distance
    else:
        print('Points do not have the same number of dimensions.')\
       
    
#example of using N-Dimensional distance function
dist = distanceN([0,0,0,0],[1,2,3,4])
print(dist)
