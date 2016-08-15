import subprocess
import os
import re
import math
import glob
from datetime import timedelta

movieDir = '/home/zhengbo/dataBase/splitMovies/outputNoSubtitle/'

def getMoviePath(rootDir):
    subFolders = os.listdir(rootDir)
    subFolders.sort(key=lambda x: int(x[:]))
    outPath = []
    for subFolder in subFolders:
        tmp=glob.glob(rootDir + subFolder + '/*')
        tmp.sort(key=lambda x: int(x[-8:-4]))
        outPath.extend(tmp)
    return outPath

if __name__ == '__main__':

    moviePaths = getMoviePath(movieDir)

    f=open('Times.txt','r')
    newTime=[]
    for line in f:
       newTime.append(int(line.strip('\n')[:-2]))
    f.close()

    f=open('Times2.txt','r')
    oldTime=[]
    for line in f:
         oldTime.append(int(line.strip('\n')[:-2]))
    f.close()

    i=0
    j=0
    toBeDel=[]
    while(i<len(oldTime)and j<len(newTime)):
        if(oldTime[i]==newTime[j]):
             i+=1
             j+=1
        elif(oldTime[i]!=newTime[j]):
             toBeDel.append(i)
             i+=1
    while(i<len(oldTime)):
        toBeDel.append(i)
        i+=1
    for movieIndex in toBeDel:
        command='rm '+moviePaths[movieIndex]
        print (command)
        os.system(command)
    print('------finish delete movie-----------\n')
    moviePaths=[]
    moviePaths = getMoviePath(movieDir)
    charName = '';
    for index in range(1,len(moviePaths)+1):
        if(index < 10):
            charName = '000'
        elif(index < 100):
            charName = '00';
        else:
            charName = '0';
        newName='ADBSZU'+charName+str(index)+'.mp4'
        command='mv ' +moviePaths[index-1]+ ' ' +moviePaths[index-1][:-12]+newName
        print (command)
        os.system(command)
    print ('-----finish move video and change name----------\n')






