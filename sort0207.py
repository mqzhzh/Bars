
import matplotlib.pyplot as plt
import numpy as np
import csv
import json


# inputs
length = list(range(0, 26))
chartPosi = 16
iterations = list(range(0, 10))
isMinLevel = 0
barScale = 26
valuePosi = 25

x = np.genfromtxt('Book1.csv',delimiter=',',dtype=None, names=True)

X_ori = np.array(x)
#  dtype=np.float64)

X = [] 
for item in X_ori:
    # print (item)
    a = list(item)
    # note: a = np.array(item) do not work well, tuple 
    # a[0] = str(a[0])
    X.append(a)
X = np.array(X) # note: type 'list' cannot do slicing [:,1:2]


# swap
X_1 = []
for item in X:
    a = list(item)
    X_1.append(a[1])
# print (X_1)

# X_1 = X[:,1:2]
chartPosiOrigi = chartPosi

shift = 0
maxIndex = []
for iteration in iterations:
   
    if isMinLevel:
        max_index = np.argmin(X_1) 
        # if max_index < chartPosiOrigi:
        #     shift -= 1
        #     print (max_index,'\n',chartPosi,'\n', shift)
        X_1[max_index] = 100000
        # print (max_index, '\n')
        if max_index < chartPosiOrigi:
            shift -= 1

    else:
        max_index = np.argmax(X_1) 
        X_1[max_index] = -100
        # print (max_index, '\n')
        if max_index < chartPosiOrigi:
            shift -= 1

        maxIndex.append(max_index)
# print (maxIndex, shift)




X = np.array(X)
Max = []
for iteration in iterations:
    # print (X[maxIndex[iteration]],'\n','\n')
    Max.append(X_ori[maxIndex[iteration]])
# print (Max)


# print (X)
X0 = list(X[:,0])
X1 = list(X[:,1])
# print (X0,X1)
X = list(X)
for iteration in iterations:
    popIndex = X0.index(maxIndex[iteration])
    X0.pop(popIndex)
    X.pop(popIndex)
    # print (popIndex,'\n', X0)
####### notes: why there is a bug of [index out of range for popping], 
# because, every time you pop out, the real index for the next number to 
# get popped out changes (if previous number is less than it, should minus sth)

###### notes: if x = y, then change x, y will change simultaneously. 
# The method to solve this is: x.append(item in y)..

#!!!!!!# UNSOVLED: target bar in the xxx largest.. miss 1 bar

chartPosi = chartPosi + shift    
# print (chartPosi,'\n', X)



insertLeft = chartPosi
for item in Max:
    if item[0] < chartPosiOrigi:
        # print ('Left', insertLeft)
        X.insert(insertLeft , item)
        chartPosi += 1
        
# print (chartPosi)   

stepRight = 1
for item in Max:   
    if item[0] > chartPosiOrigi:
        X.insert(chartPosi + stepRight, item)
        # print ('Right', stepRight + chartPosi, )
        stepRight  += 1

# X = np.array(X)
# X_1 = np.array(X_1)
# Max = np.array(Max)
# print (X, '\n', len(X))






# # simple swapping 
# for item in X:
#     if item[0] == '2':
#         a = X.index(item)
#         # print (a)
#     if item[0] == '8':
#         b = X.index(item)
#         # print (b)
# X[a], X[b] = X[b], X[a]
# print (X)

# print (type(X),X)
toRender = []

X_render = []
for item in X:
    a = list(item)
    a[0] = str(a[0])
    X_render.append(a)
print (X_render, type(X_render))


trials = list(range(0, 1))
for trial in trials:
   
    # chartPosi = 0
    # barScale = 30
    # valuePosi = 0.25
    # print (localContrast, chartPosi,barScale,valuePosi)

    
    value = {}
    value['trialNumber'] = trial

    value['localContrast'] = len(iterations)
    value['chartPosi'] = chartPosi
    value['barScale'] = barScale
    value['valuePosi'] = valuePosi
    
    # index = 0
    value['dataSource'] = []
    for item in X_render:
        
        subvalue = {}
        # subvalue['index'] = index
        subvalue['frequency']  = item[1]
        subvalue['name'] = item[0]
        # index += 1
        value['dataSource'].append(subvalue)



    toRender.append(value)

    
print (toRender)


### dump to json
with open('output.json', 'w') as f:
     f.write(json.dumps(toRender))
#### notes: cannot dump because format of [0.0] and [5] (inserted inside,
# cannot be serialized)

# ### dump to csv
# csvFile = ""

# for key, value in X:
#     csvFile += key + "," + value + '\n'
# with open('./csvFile.csv', 'w') as f:
#     f.write(csvFile.encode('utf-8'))

