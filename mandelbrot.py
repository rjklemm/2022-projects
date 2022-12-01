# Mandelbrot Set

#Bob Klemm
#11/19/2022

import matplotlib.pyplot as plt

a = range(-125,125)
b = range(-200,50)
x_values = []
y_values = []
 
for point in a:
    x_values.append(0.01 * point)
for point in b:
    y_values.append(0.01 * point)

data = []

for x in x_values:
    
    data_row = []
    
    for y in y_values:
        
        #Setup
        c = complex(y,x)
        z = 0 
        
        for i in range(1,101):
            if abs(z) > 10:
                data_row.append(i)
                break
            
            else:
                z = z**2 + c
                if i == 100:
                    data_row.append(i)
        
    data.append(data_row)    
    
plt.contour(x_values, y_values ,data, [0, 20, 40, 60, 80, 100])
plt.title('Mandelbrot Set / Quadratic Map')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')