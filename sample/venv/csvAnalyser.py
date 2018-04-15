#config: euc-kr
import sys

print("="*20)
print("writer : RYUPE")
print("DATE : 2018-04-15")
print("TITLE : CVS FILE CONVERSION")
print("="*20)

if len(sys.argv) >= 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    input_file = "cvsdata.csv"
    output_file = "cvsdata_out.csv"



with open(input_file,'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        # 첫행 타이틀 출력
        header = filereader.readline()
        header = header.lstrip()
        header = header.rstrip()
        header_list = header.split(",")
        print("READER ::", header_list)
        print("READER ::", ','.join(map(str,header_list))+'\n')
        
        filewriter.write(','.join(map(str,header_list))+'\n')


        # 데이터 부분 출력
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print("WRITE :: ", row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')
