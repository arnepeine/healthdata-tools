from pandas import read_csv

print("[")
df = read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQHr4MaIjQ7qMMAL8EvIoNLaUgLzLhfduIEDp_OLrU1Q78aQ9sEGV19H3Z2mvlP9QvECBDX2g4lkUPw/pub?gid=0&single=true&output=csv" ,names = ["oscode", "name", "category"])
print("")
for index, row in df.iterrows():
    print("{")
    print('"value":"'+row["oscode"]+'", "text": "'+row["oscode"],row["name"]+'", "class": "'+row["category"]+'", "oimid": "'+row["oscode"]+'"')
    print("},")    
print("]")
