import subprocess
import os
import re
import math
import glob
from datetime import timedelta

movieDir = '/home/zhengbo/experiment/outputNoSubtitle/'


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
    f=open('Times2.txt','w+')
    totalTimes=0
    for moviePath in moviePaths:

        # Check if movie file exists
        if(os.path.isfile(moviePath)):

            print(moviePath)
            movieDuration = getLength(moviePath)
            movieDurations = movieDuration.split(':')
            movieTimeDelta = timedelta(hours=int(movieDurations[0]), minutes=int(movieDurations[1]),
                                       seconds=int(math.floor(float(movieDurations[2]))))

            movieTotalSeconds = movieTimeDelta.total_seconds()
            f.write(str(movieTotalSeconds)+'\n')
        else:
           print('ERROR: file ' + moviePath + ' does not exist')

    f.close()
