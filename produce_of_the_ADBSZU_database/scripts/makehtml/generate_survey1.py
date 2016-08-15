#random move the file and generate the html5 video script.
import os
import glob
import random
movieDir = '/ftp/videos/'
dir_http='http://172.31.70.7/experiment/'

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

    for j in range(1,11):
        moviePaths = getMoviePath(movieDir)
        random.shuffle(moviePaths)
        outPath = '/ftp/experiment/'
        print(len(moviePaths))
        f=open(str(j)+'.txt','w+')
        if(len(moviePaths)>=40):
            last=40;
        else:
            last=len(moviePaths)
        for i in range(0,last):
             movieName=str(j)+'/'+moviePaths[i][-14:]
             if (i!= 0):
                 f.write('\n')
             info ='<video src="'+dir_http+movieName+'" '+'controls width="480" heigt="320">' \
                                                          'your brower not support html5!</video>\n'
             f.write(info)
             f.write('1\n2\n3\n4\n5\n6\n')
             commandLine=' mv '+moviePaths[i]+' '+outPath+movieName
             os.system(commandLine)
    f.close()
