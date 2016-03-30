#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np

array = [] #declaring a list with name '**array**' 
#reads in every line, removes all the new line characters, and then
#converts it into a float value
with open(sys.argv[1],'r') as reader:
    for line in reader:
        line =  line.rstrip("\n")
        array.append(float(line))
#There is a 3 second time delay between each. We just add 3 depending on
# the amount of time
time = []
seconds = 3
for temp in array:
    time.append(seconds)
    seconds = seconds + 3
#It only accepts np arrays, so I just convert it over.
x = np.array(time)
y = np.array(array)

plt.plot(x,y)
plt.ylabel('Plot of temperature data by Rex Petersen')
plt.xlabel('Time (seperated by 3 seconds)')
plt.show()
