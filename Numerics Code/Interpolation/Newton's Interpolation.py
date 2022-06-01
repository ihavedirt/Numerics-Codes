import math as m
import numpy as np

#insert parameters#######################
# val = [[2.0, 0.85467], [2.3, 0.75682], [2.6, 0.43126], [2.9, 0.22364], [3.2, 0.08567]]

x = 2.7
decimal = 4
#########################################

tempval = input('input(parse with spaces): ')

tempval = tempval.split(' ')
tempval = [float(x) for x in tempval]
val = []

for i in range(int(len(tempval)/2)):
    val.append(tempval[i*2:i*2+2])

print(val)
#----------------------

#build initial matrix
temp = []
result = np.zeros((len(val),len(val)*2))

for j in range(len(val)):
    result[0][j*2] = val[j][1]


for i in range(1,len(val)):
    for j in range(len(val)-i):
        a = result[i-1][j*2+i+1]
        b = result[i-1][j*2+i-1]
        tempResult = (a-b) / (val[j+i][0] - val[j][0])
        result[i][j*2+i] = round(tempResult,decimal)

#display result stuff
tempString = ''
for i in range(len(result)*2-1):
    tempString += '{: >10} '
tempString = tempString[:-1]

for row in result:
    print(tempString.format(*row))

#calculate Sum
sum = 0
for i in range(len(val)):
    mult = result[i][i]
    print(mult)
    for j in range(i):
        print('(x - ' + str(val[j][0]) + ')')
        mult *= (x - val[j][0])
    print()
    sum += mult

print(sum)