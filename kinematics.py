"""
Bob Klemm
5/27/2022

'Kinematics'
"""

#Solving simple kinematics problems
#g = -9.8 #meters per second squared (gravitational constant)

"""
Kinematic Equations

Constant Velocity:
x = x0 + v * t

Constant Acceleration (a = g, for projectile motion):
v = v0 + g * t
y = y0 + v0 * t + 0.5 * g * t ** 2
v = math.sqrt(v0 ** 2 + 2 * g * (y - y0) ** 2)
"""

#Constant velocity (check your units!)

def cvfindtime(x,x0,v):
    t = (x - x0) / v
    return t
    
def cvfindposition(x0,v,t):    
    x = x0 + v * t
    return x
    
def cvfindvelocity(x,x0,t):
    v = (x - x0) / t
    return v


#Constant acceleration (some cases)

def cafindvelocity(v0,a,t):
    v = v0 + a * t
    return v

def cafindposition(y0,v0,a,t):
    y = y0 + v0 * t + 0.5 * a * t ** 2
    return y

def cafindacceleration(v, v0, t):
    a = (v - v0) / t
    return a

#Common unit conversions for velocity

#m/s and mi/hr
def mstomihr(a):
    c = 2.23694
    b = c * a
    return b

def mihrtoms(a):
    c = 2.23694
    b = a / c
    return b

#m/s and ft/s
def mstofts(a):
    c = 3.28084
    b = c * a
    return b

def ftstoms(a):
    c = 3.28084
    b = a / c
    return b

