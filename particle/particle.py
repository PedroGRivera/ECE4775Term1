import random
import math
import numpy as np
import threading
import time
import os
import sys
import psutil

#sys.argv
#1 = size
#2 = mnum
#3 = iter
#4 = 
#5 = 
#6 = 
state = False
size = int(sys.argv[1])#100
hmax = 1
hmin = 0
mNum = size*1000#int(sys.argv[2])#100000
iVal = 0.001
b    = 1
bVal = iVal*b

def log():
    global state
    try:
        os.system('rm /mnt/f/algTerm1/data/ParticleDataS' + str(size) + '-M' + str(mNum) + '-I' + sys.argv[2] + '.csv')
    except: pass
    f = open('/mnt/f/algTerm1/data/ParticleDataS' + str(size) + '-M' + str(mNum) + '-I' + sys.argv[2] + '.csv','a')
    f.write('time,cpu,mem\n')
    while state:
        f.write(str(time.time()) + ',' + str(psutil.cpu_percent()) + ',' + str(psutil.virtual_memory().used) + '\n')
        time.sleep(0.1)
    f.close()


arr = np.zeros((size,size))

#ul  uc  ur
#ml (pt) mr
#dl  dc  dr
def getNeighbor(x,y):
    global arr
    pos = {'ul':[None,None],'uc':[None,None],'ur':[None,None],'ml':[None,None],'mr':[None,None],'dl':[None,None],'dc':[None,None],'dr':[None,None]}
    if x != 0 and y != 0 :
        pos['ul'][0] = x-1
        pos['ul'][1] = y-1
    if x != 0 :
        pos['ml'][0] = x-1
        pos['ml'][1] = y
    if x != 0 and y < len(arr)-1 :
        pos['dl'][0] = x-1
        pos['dl'][1] = y+1
    if y != 0 :
        pos['uc'][0] = x
        pos['uc'][1] = y-1
    if y < len(arr)-1 :
        pos['dc'][0] = x
        pos['dc'][1] = y+1
    if x < len(arr[0])-1 and y != 0 :
        pos['ur'][0] = x+1
        pos['ur'][1] = y-1
    if x < len(arr[0])-1 :
        pos['mr'][0] = x+1
        pos['mr'][1] = y
    if x < len(arr[0])-1 and y < len(arr)-1 :
        pos['dr'][0] = x+1
        pos['dr'][1] = y+1
    rem = []
    for i in pos:
        if pos[i][0] == None and pos[i][1] == None:
            rem.append(i)
    for i in rem:
        pos.pop(i)
    #print(pos)
    return pos

#returns true if the center is too high
#return false if the center is not too high
def bFail(x,y,pos):
    global arr
    global iVal
    global bVal
    for i in pos:
        if arr[x][y] + iVal > arr[pos[i][0]][pos[i][1]] + bVal:
            return True
    return False

def getLowestNeighbor(x,y, pos):
    global arr  
    global hmax
    low = [None,None]
    lowVal = hmax*2
    for i in pos:
        if arr[pos[i][0]][pos[i][1]] < lowVal:
            low[0] = pos[i][0]
            low[1] = pos[i][1]
            lowVal = arr[low[0]][low[1]]
    return low

# arr[1][1] = bVal-iVal
# pos = getNeighbor(1,1)
# print(pos)
# print(bFail(1,1,pos))
# print(getLowestNeighbor(1,1,pos))


def move(x,y):
    global arr
    pos = getNeighbor(x,y)
    if bFail(x,y,pos):
        nxt = getLowestNeighbor(x,y,pos)
        move(nxt[0], nxt[1])
    else:
        arr[x][y] += iVal


def run():
    for i in range(0,mNum):
        x0 = random.randint(0,size-1)
        y0 = random.randint(0,size-1)
        #print(x0)
        #print(y0)
        move(x0,y0)

        if arr[x0][y0] > hmax:
            arr[x0][y0] = hmax

state = True
thread = threading.Thread(target=log)
thread.start()
run()
state = False
thread.join()

dat = open('/mnt/f/algTerm1/files/Particle.csv', 'w')
dat.write(','.join(str(v) for v in list(range(0,size))) + '\n')
for i in arr:
    dat.write(','.join(str(v) for v in i)+ '\n')
