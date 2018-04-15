#config: euc-kr
import sys
import pandas as pd


print("="*20)
print("writer : RYUPE")
print("DATE : 2018-04-15")
print("TITLE : CVS FILE CONVERSION form PANDAS")
print("="*20)

if len(sys.argv) >= 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    input_file = "cvsdata.csv"
    output_file = "cvsdata_out_pandas.csv"

data_frame = pd.read_csv(input_file, encoding='euc-kr')
print(data_frame)
data_frame.to_csv(output_file, index=False, encoding='euc-kr')



