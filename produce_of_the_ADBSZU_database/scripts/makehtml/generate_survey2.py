# coding=utf-8 ##
#form the subfloder generate the html script.
import os
import glob
import random
movieDir = '/ftp/experiment/'
dir_http='http://172.31.70.7/'

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

    for i in range(0,10):
        f=open(str(i)+'.txt','w+')
        for j in range(0,40):
            if (j!= 0):
                f.write('\n')
            temp=i*40+j;
            if(temp>=len(moviePaths)):
                break
            else:
                info='<a href="'+dir_http+moviePaths[temp][5:]+' target="_blank">'+'视频'+str(j+1)+'</a>'+'\n'
                f.write(info)
                f.write('1\n2\n3\n4\n5\n6\n')
        f.close()
