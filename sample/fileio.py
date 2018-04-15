f = open('newfile.txt', 'w')
for i in range(1,11):
    f.write("12345 %d 라인\n" %(i))
f.close()

fileData = ''
f = open('newfile.txt', 'r')
while True:
    num = 0
    line = f.readline()
    if not line: break
    print(line, end='')
    fileData += line

f.close()


find = fileData.count('라인')
print('라인은 %d번 포함되어있습니다.' %find)

# while True:
#     find = fileData.find('라인')
#     if not find: break
#     print('라인이 포함된 문자열은 %d 줄입니다.' %find)
#
# fileData.fileData


