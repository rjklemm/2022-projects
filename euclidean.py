"""
Bob Klemm
5/27/2022

'Euclidean Distance'
"""

from ast import Return
import math

#2D distance
#inputs are two 1x2 vectors with point coordinates
def distance2(point1, point2):
    if len(point1) == len(point2):
        xdiff = point2[0] - point1[0]
        ydiff = point2[1] - point1[1]
        distance = math.sqrt(xdiff**2 + ydiff**2)
        return distance
    else:
        print('Points do not have the same number of dimensions.')
        

#example of using 2D distnace function
dist = distance2([0,0],[3,4])
print(dist)


#3D distance
#inputs are two 1x3 vectors with point coordinates
def distance3(point1, point2):
    if len(point1) == len(point2):
        xdiff = point2[0] - point1[0]
        ydiff = point2[1] - point1[1]
        zdiff = point2[2] - point1[2]
        distance = math.sqrt(xdiff**2 + ydiff**2 + zdiff**2)
        return distance
    else:
        print('Points do not have the same number of dimensions.')
        

#example of using 3D distance function
dist = distance3([0,0,0],[3,4,5])
print(dist)


#N-dimesional distance
#inputs are two 1xN vectors with point coordinates
def distanceN(point1, point2):
    if len(point1) == len(point2):
        sum = 0
        for i in range(0,len(point1)):
            diff = point2[i] - point1[i]
            sum += diff**2
        distance = math.sqrt(sum)
        return distance
    else:
        print('Points do not have the same number of dimensions.')\
       
    
#example of using N-Dimensional distance function
dist = distanceN([0,0,0,0],[1,2,3,4])
print(dist)
