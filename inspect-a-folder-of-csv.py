from pandas import read_csv
from matplotlib import pyplot
import random
import glob, os
dir ='/to/dir/'
a = open(dir+"output.csv", "w")
os.chdir(dir)
for file in glob.glob("*.csv"):
    print(file)
    a.write(file + ",,\n")
    df = read_csv(dir+file)
    df.hist()
    pyplot.show()
    sorted_up = df.sort_values(by=df.columns[2],ascending=0)
    sorted_down = df.sort_values(by=df.columns[2],ascending=1)
    print(sorted_up.head(5))
    print(df.take(random.sample(range(1, len(df.index)), 5)))
    print(sorted_down.head(5))
