import random
import math
import numpy as np
import os
import sys
import time
import psutil
import threading
#sys.argv
#1 = size
#2 = iter

size = int(sys.argv[1])#500
hmax = size
hmin = 0
state = False

def log():
    global state
    try:
        os.system('rm /mnt/f/algTerm1/data/limRandDataS' + str(size) + '-I' + sys.argv[2] + '.csv')
    except: pass
    f = open('/mnt/f/algTerm1/data/limRandDataS' + str(size) + '-I' + sys.argv[2] + '.csv','a')
    f.write('time,cpu,mem\n')
    while state:
        f.write(str(time.time()) + ',' + str(psutil.cpu_percent()) + ',' + str(psutil.virtual_memory().used) + '\n')
        time.sleep(0.1)
    f.close()

arr = np.zeros((size,size))

def run():
    for i in range(0,size-1):
        for j in range(0,size-1):
            a = 0
            if i != 0 and j != 0:
                a = (arr[i-1][j]+arr[i][j-1])/2
            elif  i != 0 and j == 0:
                a = arr[i-1][j]
            else:
                a = random.uniform(0,hmax/10)
            h = a + (hmax/10)*random.uniform(-1,1)
            arr[i][j] = max([0,min([h,hmax])])


state = True
thread = threading.Thread(target=log)
thread.start()
run()
state = False
thread.join()


dat = open('/mnt/f/algTerm1/files/limRand.csv', 'w')
dat.write(','.join(str(v) for v in list(range(0,size))) + '\n')
for i in arr:
    dat.write(','.join(str(v) for v in i)+ '\n')
dat.close()
