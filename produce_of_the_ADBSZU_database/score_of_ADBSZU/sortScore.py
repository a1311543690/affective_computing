# since the score is record by groub, these groub is randon set
# this script sort the score use the original id
f=open('groubIname.txt','r')
groubFile=[]
for line in f:
    line=line.strip()
    temp=int(line[-8:-4])
    groubFile.append(temp)
f.close()

f=open('score.txt','r')
scores=[]
for line in f:
    scores.append(line)
f.close()

n=len(scores)
m=50
results=[None]*n
for i in range(len(results)):
    results[i]=[None]*m
#print results

for i in range(n):
    index=groubFile[i]
    results[index-1]=scores[i]

f=open('scoreOrded.txt','w+')
for element in results:
    f.write(element)
f.close()