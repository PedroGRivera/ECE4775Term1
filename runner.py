import os
import sys
import time

iterStart = 0
iterSize = 5
size = [((2**i)) for i in range(7,9)]
files = ["./generation/fault.py","./hills/circle.py","./limitedRand/limitRand.py","./particle/particle.py","./midpoint/midpoint.py"]

start = time.time()
for i in range(iterStart,iterSize):
    print("-------------------------------------------------------------------------------------")
    print(i)
    print("-------------------------------------------------------------------------------------")
    for s in size:
        #print('i:' + str(i) + ' -- s:' + str(s))
        os.system("python3 " + files[0] + " " + str(s) + " " + str(i) )
        os.system("python3 " + files[1] + " " + str(s) + " " + str(i) )
        os.system("python3 " + files[2] + " " + str(s) + " " + str(i) )
        os.system("python3 " + files[3] + " " + str(s) + " " + str(i) )
        os.system("python3 " + files[4] + " " + str(s) + " " + str(i) )
        
end = time.time()

print('Total Time:' + str(end-start))
###########################################
###########################################
###########################################
###########################################
#total execution time is: 678.4546332359314
###########################################
###########################################
###########################################
###########################################