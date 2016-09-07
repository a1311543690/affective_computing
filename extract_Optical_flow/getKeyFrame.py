import subprocess
import os
import re
import math
import glob

movieDir = '/home/zhengbo/dataBase/splitMovies/outputNoSubtitle/'
outFolder= 'Frames1/'

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
    moviePaths.sort(key=lambda x: int(x[-8:-4]))

    for moviePath in moviePaths:
    	if os.path.isfile(moviePath):
    	    print(moviePath)
    	    movieName=moviePath[-14:-4]
    	    outPut=outFolder+movieName+'/'
            if not os.path.exists(outPut):
    	        os.makedirs(outPut)
    	    command='ffmpeg -loglevel error -i ' + moviePath + ' -vf fps=1 -q:v 2 ' + outPut +movieName+'-%4d.jpg'
    	    #print(command)
            os.system(command)    
        else:
           print('ERROR: file ' + moviePath + ' does not exist')
