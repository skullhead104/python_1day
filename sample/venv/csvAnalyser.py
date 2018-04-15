import sys


print(len(sys.argv))

if len(sys.argv) >= 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    input_file = "cvsdata.csv"
    output_file = "cvsdata_out.csv"



with open(input_file,'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.lstrip()
        header_list = header.split(",")
        print(header_list)

        filewriter.write(','.join(map(str,header_list))+'\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')
