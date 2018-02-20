# Convert CSV to JSON
from pandas import read_csv
i=1
print("[")
df = read_csv("file.csv" ,names = ["number","oscode", "name", "category"])
for index, row in df.iterrows():
    print("{")
    print('"value":"'+ str(row["number"]) +'", "text": "'+row["oscode"],row["name"]+'", "class": "'+row["category"]+'", "oimid": "'+row["oscode"]+'"') 
    if i == len(df):
        print("}") 
    else:
        print("},")
    i+=1
print("]")
