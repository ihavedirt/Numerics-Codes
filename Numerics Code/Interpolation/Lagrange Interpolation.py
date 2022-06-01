import math as m

#insert parameters#######################
# val = [[,],
#        [,],
#        [,],
#        [,],
#        [,]]

x = 2.23
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


result = 0

for i in range(len(val)):
    lagrange = val[i][1]
    print(lagrange)
    for j in range(len(val)):
        if j != i:
            lagrange *= (x-val[j][0])/(val[i][0]-val[j][0])
            print('(x-' + str(val[j][0]) + ')/(' + str(val[i][0]) + '-' + str(val[j][0]) + ')')
    print('term: ' + str(round(lagrange,decimal)))
    print()
    result += lagrange

print('Final Result: ' + str(round(result,decimal)))
