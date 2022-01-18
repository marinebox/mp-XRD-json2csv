from fileinput import filename
import pandas as pd
import json
import os


def json2csv(filename: str = None):
    name = filename[:-5]
    jsonFile = open(filename)
    js = json.load(jsonFile)
    patterns = js['pattern']
    data = []
    for pattern in patterns:
        t = pattern[2]
        a = pattern[0]
        data.append([t, a])
    df = pd.DataFrame(data, columns=['two_theta', 'amplitude'])
    df.to_csv(name + '.csv')
    return


jsonFiles = [j for j in os.listdir('.') if j[-5:] == '.json']
jsonFiles.sort()

for i, e in enumerate(jsonFiles):
    print(i, e)

fileNum = int(input('which json file convert? enter number: '))
filename = jsonFiles[fileNum]
json2csv(filename)

print('accomplished!')
