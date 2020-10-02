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
#2 = fnum
#3 = iter
#4 = 
#5 = 
#6 = 




size = int(sys.argv[1])#500
c = 0.001
hmax = 1
hmin = 0
fNum = int(int(size)*2)#int(sys.argv[2])#100
state = False
#logFile = sys.argv[3]


def log():
    global state
    try:
        os.system('rm /mnt/f/algTerm1/data/FaultDataS' + str(size) + '-F' + str(fNum) + '-I' + sys.argv[2] + '.csv')
    except: pass
    f = open('/mnt/f/algTerm1/data/FaultDataS' + str(size) + '-F' + str(fNum) + '-I' + sys.argv[2] + '.csv','a')
    f.write('time,cpu,mem\n')
    while state:
        f.write(str(time.time()) + ',' + str(psutil.cpu_percent()) + ',' + str(psutil.virtual_memory().used) + '\n')
        time.sleep(0.1)
    f.close()

arr = np.zeros((size,size))

def run():

    for i in range(0,fNum):
        x0 = random.randint(0,size)
        y0 = random.randint(0,size)
        x1 = x0
        y1 = y0
        while x1 == x0:
            x1 = random.randint(0,size)
        while y1 == y0:
            y1 = random.randint(0,size)
        #print('x0:' + str(x0) + ' - y0:' + str(y0) + ' - x1:' + str(x1) + ' - y1:' + str(y1) )
        for xVal in range(0, len(arr)):
            for yVal in range(0, len(arr[xVal])):
                if ((x1-x0)*(yVal-y0) - (y1-y0)*(xVal-x0))  > 0:
                    arr[xVal][yVal] += c
                else:
                    arr[xVal][yVal] -= c
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


dat = open('/mnt/f/algTerm1/files/Fault.csv', 'w')
dat.write(','.join(str(v) for v in list(range(0,size))) + '\n')
for i in arr:
    dat.write(','.join(str(v) for v in i)+ '\n')

dat.close()