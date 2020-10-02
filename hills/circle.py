import math
import random
import numpy as np
import psutil
import os
import string
import threading
import time
import sys


#sys.argv
#1 = size
#2 = hnum
#3 = iter
#4 = 
#5 = 
#6 = 

size = int(sys.argv[1])#100
r = 2*(size/10)
hmax = 1
hmin = 0
s = 0.015
hNum = int(size)#int(sys.argv[2])#200
state = False

def log():
    global state
    try:
        os.system('rm /mnt/f/algTerm1/data/CircleDataS' + str(size) + '-H' + str(hNum) + '-I' + sys.argv[2] + '.csv')
    except: pass
    f = open('/mnt/f/algTerm1/data/CircleDataS' + str(size) + '-H' + str(hNum) + '-I' + sys.argv[2] + '.csv','a')
    f.write('time,cpu,mem\n')
    while state:
        f.write(str(time.time()) + ',' + str(psutil.cpu_percent()) + ',' + str(psutil.virtual_memory().used) + '\n')
        time.sleep(0.1)
    f.close()

arr = np.zeros((size,size))

def run():
    for i in range(0,hNum):
        x0 = random.randint(0,size)
        y0 = random.randint(0,size)
        x1 = x0
        y1 = y0
        for xVal in range(0, len(arr)):
            for yVal in range(0, len(arr[xVal])):
                d = ((x0-xVal)**2)+((y0-yVal)**2)
                if d < r**2:
                    arr[xVal][yVal] += (s/2.0)*(1+ math.cos((math.pi*d)/(r**2)))
                if arr[xVal][yVal] > hmax:
                    arr[xVal][yVal] = hmax
                if arr[xVal][yVal] < hmin:
                    arr[xVal][yVal] = hmin

state = True
thread = threading.Thread(target=log)
thread.start()
run()
state = False
thread.join()

dat = open('/mnt/f/algTerm1/files/Circle.csv', 'w')
dat.write(','.join(str(v) for v in list(range(0,size))) + '\n')
for i in arr:
    dat.write(','.join(str(v) for v in i)+ '\n')
dat.close()