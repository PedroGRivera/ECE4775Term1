import random
import numpy as np
import psutil
import os
import string
import threading
import time
import sys
from datetime import datetime

random.seed(datetime.now())

#sys.argv
#1 = size
#2 = iter

size = int(sys.argv[1])#(2**1)+1
hmax = 100
arr = np.ones((size,size))

def log():
    global state
    try:
        os.system('rm /mnt/f/algTerm1/data/midpointDataS' + str(size) + '-I' + sys.argv[2] + '.csv')
    except: pass
    f = open('/mnt/f/algTerm1/data/midpointDataS' + str(size) + '-I' + sys.argv[2] + '.csv','a')
    f.write('time,cpu,mem\n')
    while state:
        f.write(str(time.time()) + ',' + str(psutil.cpu_percent()) + ',' + str(psutil.virtual_memory().used) + '\n')
        time.sleep(0.1)
    f.close()

def diamond(x,y,dist):
    global size
    global arr
    cnt = 0.0
    avg = 0.0
    if x-dist >= 0:
        cnt += 1
        avg += arr[x-dist][y]
    if x+dist < size:
        cnt += 1
        avg += arr[x+dist][y]
    if y-dist >= 0:
        cnt += 1
        avg += arr[x][y-dist]
    if y+dist < size:
        cnt += 1
        avg += arr[x][y+dist]
    arr[x][y] = round( (avg/cnt)) + ((random.randint(0,dist))-(dist/2)) 

def square(x,y,dist):
    global size
    global arr
    cnt = 0.0
    avg = 0.0
    if x-dist >= 0:
        if y-dist >= 0:
            cnt += 1
            avg += arr[x-dist][y-dist]
        if y+dist < size:
            cnt += 1
            avg += arr[x-dist][y+dist]
    if x+dist < size:
        if y-dist >= 0:
            cnt += 1
            avg += arr[x+dist][y-dist]
        if y+dist < size:
            cnt += 1
            avg += arr[x+dist][y+dist]
    arr[x][y] = round( (avg/cnt) )  + ((random.randint(0,dist))-(dist/2)) 

def step(sizeV):
    global size
    global arr
    half = int(sizeV/2)
    #break state
    if half < 1:
        return
    #square step
    for x in range(half, size, sizeV):
        for y in range(half, size, sizeV):
            square(x,y,half)
    #diamond step
    for x in range(0, size, half):
        start = 0
        if (int(x/half)+1)%2 == 1:
            start = half
        for y in range(start,size,sizeV):
            diamond(x,y, half)
        #case where x = middle row
        ##the right most point is not calculated
        ##so the code below will calculate this
        if sizeV == size:
            diamond(half,size-1,half)
    #recurse
    step(int(sizeV/2))

def run():
    arr[0][0]           = random.randint(0,hmax)
    arr[0][size-1]      = random.randint(0,hmax)
    arr[size-1][0]      = random.randint(0,hmax)
    arr[size-1][size-1] = random.randint(0,hmax)
    step(size)

state = True
thread = threading.Thread(target=log)
thread.start()
run()
state = False
thread.join()

dat = open('/mnt/f/algTerm1/files/midPoint.csv', 'w')
dat.write(','.join(str(v) for v in list(range(0,size))) + '\n')
for i in arr:
    dat.write(','.join(str(v) for v in i)+ '\n')

dat.close()