"""
Bob Klemm
5/27/2022

'Acoustics'
"""

import math
import matplotlib.pyplot as plt

a = [1, 1, 1] #amplitude vector for different notes
f = [261.63, 349.23, 392.00] #frequency vector for different notes
names = ['C4', 'F4', 'G4']#names vector for the names of notes

n = 500 #data points per 4pi (double wavelength)
tf = 0.3 #final time

moment = []
for index in range(0,n):
    moment.append(tf*index / 1000)

y = [] #waves

for wave in range(0,len(names)):
    y1 = []
    for point in moment:
        y0 = a[wave] * math.cos(f[wave] * point)
        y1.append(y0)
    y.append(y1)
for wave in range(0,len(y)):
    plt.plot(moment,y[wave])
plt.xlabel('Time')
plt.ylabel('Waveform')
plt.legend(names)
plt.title('Soundwave Over Time for C4, F4, and G4')
