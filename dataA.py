import os
import sys
import numpy as np

path = '/mnt/f/algTerm1/data/'



f = open('/mnt/f/algTerm1/analysis.csv','w')
f.close()
f = open('/mnt/f/algTerm1/analysis.csv','w')
f.write('algorithm,mapSize,iteration,dataSize,time,cpuAvg,memAvg\n')


# for i in os.listdir(path):
#     if i.find('S50') > -1 or i.find('S75') > -1 :
#         os.system('rm ' + path + i)

for i in os.listdir(path):
    dat = np.genfromtxt(path+i,delimiter=',', skip_header=1)
    if dat.size == 0:
        print(i)
    #print(dat)
    if dat.size != 0:
        #print(i)
        mean = dat.mean(axis=0)
        timeDiff = 0
        if not isinstance(dat[0], np.ndarray):
            #print(i)
            mean = dat
            timeDiff = 0.100000
        else:
            timeDiff = dat[int(dat.size/3)-1][0]-dat[0][0]
        #print("Size:" + str(round(dat.size,2)) + '\t\tTime(s):' + str(round(timeDiff,2)) + '\t\tCPU-avg(%):' + str(round(mean[1],2)) + "\t\tMEM-avg(MB):" + str(round(mean[2]*(10**-6),2)))
        #print("------------------------------------------------------------------------------------------")
        f.write(i[0:i.find("S")] + ',' + i[i.find('S')+1:i.find('-')] + ',' + i[i.find('I')+1:i.find('.csv')] + ',' + str(round(dat.size,2)) + ',' + str(round(timeDiff,2)) + ',' + str(round(mean[1],2)) + "," + str(round(mean[2]*(10**-6),2)) + '\n')
f.close()


dat = np.genfromtxt('/mnt/f/algTerm1/analysis.csv',dtype=None,delimiter=',',skip_header=1)
f = open('/mnt/f/algTerm1/finalInfo.csv','w')
f.close()
f = open('/mnt/f/algTerm1/finalInfo.csv','w')
f.write('testName,time(s),cpu(%),mem(MB)\n')

datDict = {}
for i in dat:
    #print(i)
    if str(i[0].decode('utf-8')) + str(i[1]) in datDict:
        datDict[ str(i[0].decode('utf-8')) + str(i[1]) ].append([i[4],i[5],i[6]])
    else:
         datDict[ str(i[0].decode('utf-8')) + str(i[1]) ]=[[i[4],i[5],i[6]]]

finalDict = {}
for i in datDict:
    #print(i + "---" + str(datDict[i]))
    timeAvg = 0.0
    cpuAvg = 0.0
    memAvg = 0.0
    cnt = 0
    for j in datDict[i]:
        cnt += 1
        timeAvg += j[0]
        cpuAvg  += j[1]
        memAvg  += j[2]
    timeAvg /= cnt
    cpuAvg  /= cnt
    memAvg  /= cnt
    #print(i + "---" + str(round(timeAvg,2)) + " " + str(round(cpuAvg,2)) + " " + str(round(memAvg,2)) )
    f.write(i+','+ str(round(timeAvg,2)) + "," + str(round(cpuAvg,2)) + "," + str(round(memAvg,2)) + '\n')
    finalDict[i] = [round(timeAvg,2),round(cpuAvg,2), round(memAvg,2)]
f.close()

#find fastest and slowest for each size
fastest = ''
f = 100000
slowest = ''
s = -1
for i in finalDict:
    #print(i + ',' + str(finalDict[i][0]) + ',' + str(finalDict[i][1]) + ',' + str(finalDict[i][2]))
    if finalDict[i][0] < f:
        fastest = i
        f = finalDict[i][0]
    if finalDict[i][0] > s:
        slowest = i
        s= finalDict[i][0]
print('fastest is: ' + fastest)
print('slowest is: ' + slowest)
print('------------------------')
#find lowest and highest cpu usage
lowest = ''
l = 101.0
highest = ''
h = -1
for i in finalDict:
    #print(i + ',' + str(finalDict[i][0]) + ',' + str(finalDict[i][1]) + ',' + str(finalDict[i][2]))
    if finalDict[i][1] < l:
        lowest = i
        l = finalDict[i][1]
    if finalDict[i][1] > h:
        highest = i
        h = finalDict[i][1]
print('lowest CPU is: '  + lowest)
print('highest CPU is: ' + highest)
print('------------------------')
#find lowest and highest mem usage
lowest = ''
l = 32000
highest = ''
h = -1
for i in finalDict:
    #print(i + ',' + str(finalDict[i][0]) + ',' + str(finalDict[i][1]) + ',' + str(finalDict[i][2]))
    if finalDict[i][2] < l:
        lowest = i
        l = finalDict[i][2]
    if finalDict[i][2] > h:
        highest = i
        h = finalDict[i][2]
print('lowest MEM is: '  + lowest)
print('highest MEM is: ' + highest)
print('------------------------')