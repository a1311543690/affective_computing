import subprocess
import os
import re
import math
import glob
from datetime import timedelta

movieDir = '/home/zhengbo/dataBase/splitMovies/outputNoSubtitle/'


def getLength(filename):

    result = subprocess.Popen(["ffprobe", filename], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    (stdout, stderr) = result.communicate()

    entries = stdout.decode('utf-8').split('\n')

    for line in entries:

        if(re.search('Duration', line)):

            segments = line.split(',')
            duration = segments[0].replace('  Duration: ','')
            return duration
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
    charName = '';
    for index in range(0,len(moviePaths)):
        if(index < 10):
            charName = '000'
        elif(index < 100):
            charName = '00';
        else:
            charName = '0';
        newName='ADBSZU'+charName+str(index+1)+'.mp4'
        command='mv ' +moviePaths[index]+ ' ' +moviePaths[index][:-14]+newName
        print (command)
        os.system(command)
    print ('finish')






