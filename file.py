import pandas as pd
import numpy as np
import sys

collection = pd.read_csv(sys.argv[1])
collection = collection.sort_values(by=['cardcode'])
collection["cardq"] = np.where(collection["cardq"]>3, 3, collection["cardq"])
deck = "pool1.ydk"

print(collection.iloc[1:400])

f = open(deck, "w")
f.close()

for index, row in collection.iterrows():
    f = open(deck, "a")
    for i in range(row["cardq"]):
        f.write(str(row["cardid"]))
        f.write("\n")

i = 0
lines_per_file = 60
smallfile = None
with open(deck) as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = '{}.ydk'.format(i)
            i = i+1
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()

