import subprocess
import os
import re
import math
import glob
from datetime import timedelta

movieFolder = 'videos//'


# Extract the duration of a movie
# /!\ Requires FFMPEG
def getLength(filename):
    result = subprocess.Popen(["ffprobe", filename], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    (stdout, stderr) = result.communicate()

    entries = stdout.decode('utf-8').split('\n')
    for line in entries:
        if(re.search('Duration', line)):
            #print(line)

            segments = line.split(',')
            duration = segments[0].replace('  Duration: ','')

            return duration

# Extract the duration of a movie
# /!\ Requires FFMPEG
def cutMovie(moviePath, startSecond, endSecond, outputPath):

    #Example: ffmpeg -i input.mp4 -ss 00:00:30.0 -to 00:00:40.0 -y output.mp4
    #commandLine = 'ffmpeg -loglevel error -i "' + moviePath + '" -ss ' + str(startSecond) + ' -to ' + str(endSecond) + ' -y "' + outputPath + '"'
    commandLine = 'ffmpeg -loglevel error -i "' + moviePath + '" -ss ' + str(startSecond) + ' -to ' + str(endSecond) + ' -c:a aac "' + outputPath + '"'
    os.system(commandLine)

if __name__ == '__main__':

    #movieNames = []
    #f=open("movies.txt","r")
    #for line in f:
        #movieName=line.strip()
        #movieNames.append(movieName)
    moviePaths=glob.glob(movieFolder+'*')

    for moviePath in moviePaths:

        #moviePath = movieFolder + movie
        outputFolder = 'output//'+moviePath[-6:-4]+'//'
        if not os.path.exists(outputFolder):
            os.makedirs(outputFolder)
        movieFormat = moviePath[-4:]
        # Check if movie file exists
        if(os.path.isfile(moviePath)):
            #print(moviePath)

            # Split the movie in small segments every second (each one second in duration)
            movieDuration = getLength(moviePath)

            movieDurations = movieDuration.split(':')
            movieTimeDelta = timedelta(hours=int(movieDurations[0]), minutes=int(movieDurations[1]),
                                       seconds=int(math.floor(float(movieDurations[2]))))

            movieTotalSeconds = movieTimeDelta.total_seconds()
            videoTime=[0]
            timeFile='times//'+moviePath[-6:-4]+'.txt'
            f=open(timeFile,'r')
            for line in f:
                time=line.strip()
                time=time.split(':')
                t=int(time[0])*3600+int(time[1])*60+int(time[2])
                videoTime.append(t)
            f.close()
            print('Splitting ' + moviePath + ' in ' + str(len(videoTime)-1) + ' files... Please Wait.')

            for idx in range(len(videoTime)-1):
                charName = ''
                if(idx < 10):
                  charName = '0000'
                elif(idx < 100):
                  charName = '000'
                elif(idx < 1000):
                  charName = '00'
                elif(idx < 10000):
                  charName='0'
                #print(timedelta(seconds=videoTime[idx]),timedelta(seconds=videoTime[idx+1]))
                outputPath = outputFolder + moviePath[-6:-4] + '_' + charName + str(idx) + '.mkv'
                cutMovie(moviePath, timedelta(seconds=videoTime[idx]), timedelta(seconds=videoTime[idx+1]), outputPath)
        else:
          print('ERROR: file ' + moviePath + ' does not exist')
