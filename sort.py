import matplotlib.pyplot as plt
import numpy as np
import csv
import json


x = np.genfromtxt('Book1.csv',delimiter=',',dtype=None, names=True)

X_ori = np.array(x)
# dtype=np.float64)

X = []

sum = 0

for item in X_ori:
    # print (item)
    a = list(item)
    a[0] = str(a[0])
    X.append(a)
# print(X)

for item in X:
    if item[0] == '2':
        a = X.index(item)
        # print (a)
    if item[0] == '8':
        b = X.index(item)
        # print (b)
X[a], X[b] = X[b], X[a]

print (X)



toRender = {}

trials = list(range(0, 3))
for trial in trials:
    localContrast = 0
    chartPosi = 0
    barScale = 30
    valuePosi = 0.25
    toRender[trial] = {}
    toRender[trial]['trialNumber'] = trial

    toRender[trial]['localContrast'] = 0
    toRender[trial]['chartPosi'] = 0
    toRender[trial]['barScale'] = 30
    toRender[trial]['valuePosi'] = 0.25
    
    index = 0
    toRender[trial]['data'] = {}
    for item in X:
        name = item[0]
        toRender[trial]['data'][name] = {}    
        toRender[trial]['data'][name]['index'] = index
        toRender[trial]['data'][name]['frequency']  = item[1]
        index += 1

    
# print (toRender)

### dump to json
with open('output.json', 'w') as f:
     f.write(json.dumps(toRender))

# ### dump to csv
# csvFile = ""

# for key, value in X:
#     csvFile += key + "," + value + '\n'
# with open('./csvFile.csv', 'w') as f:
#     f.write(csvFile.encode('utf-8'))


# trial = 0
# localContrast = 0
# chartPosi = 0
# barScale = 30
# valuePosi = 0.25
# toRender['trial'] = {}
# toRender['trial']['trialnumber'] = trial

# toRender['trial']['localContrast'] = 0
# toRender['trial']['chartPosi'] = 0
# toRender['trial']['barScale'] = 30
# toRender['trial']['valuePosi'] = 0.25
# index = 0
# toRender['trial']['data'] = {}
# for item in X:
#     name = item[0]
#     toRender['trial']['data'][name] = {}    
#     toRender['trial']['data'][name]['index'] = index
#     toRender['trial']['data'][name]['frequency']  = item[1]
#     index += 1