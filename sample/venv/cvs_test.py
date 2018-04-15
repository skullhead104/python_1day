#config: euc-kr
import datetime
import random

datas = []



for i in range(1,11):
    datas.append(('공급자_%d'  %i,'00%d-1001' %i, int(random.random() * 10000 + 1), '$'+str(int(random.random() * 1000 + 1))+'.00', datetime.datetime.today().strftime("%Y-%m-")+str(int(random.random() * 10 + 1))))

strdata = ''
for row in datas:
    for item in row:
        strdata += str(item)+","
    strdata += "\n"
print(strdata)
print(strdata.split("\n"))
print(strdata.split(","))
