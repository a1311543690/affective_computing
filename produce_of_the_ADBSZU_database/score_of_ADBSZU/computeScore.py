# coding=utf-8 ##
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import xlrd
data=xlrd.open_workbook(unicode('打分.xlsx','utf-8'))

# get the sheel from excel
sheels = data.sheets()
#write the movie class and score to file
f=open('score.txt','w+')
# f.write('电影类型\t\t'+'打分\n')
for sheel in sheels:
    rows=sheel.nrows
    for i in range(rows):
        temp=sheel.row_values(i)
        if(temp[0][0:3]==temp[1][0:3]):
            f.write(temp[0][0:3]+'\t\t\t')
        else:
            f.write(temp[0][0:3] + '/'+ temp[1][0:3]+ '\t')
        f.write(str((float(temp[0][-1])+float(temp[1][-1]))/2)+'\n')
    # f.write('--------------------------------------------------\n')
f.close()