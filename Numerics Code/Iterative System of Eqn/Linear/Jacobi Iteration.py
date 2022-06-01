import math as m

count = 0

#insert starting x##################

#starting x vals
x = [count,0,0,0,0]

tol = 0.000001
limit = 50
###########################

play = True

tempString = ''
for i in range(len(x)):
    tempString += '{: >20} '
tempString = tempString[:-1]

while play:

    print(tempString.format(*x))

    #add or remove tolerance check#################
    if count > 0:
        tempPlay = []
        for i in range(1,len(x)):
            if abs(x[i] - temp[i]) < tol:
                tempPlay.append(False)
            else:
                tempPlay.append(True)
        if True not in tempPlay:
            play = False

    if count > limit:
        play = False
        print('max iterations reached')

    count += 1
    x[0] = count
    temp = x.copy()

    #insert eqns here##################
    g1 = 1/10*x[2] - 1/5*x[3] + 3/5
    g2 = 1/11*x[1] + 1/11*x[3] - 3/11*x[4] + 25/11
    g3 = -1/5*x[1] + 1/10*x[2] + 1/10*x[4]-11/10
    g4 = -3/8*x[2] + 1/8*x[3] + 15/8

    g = [g1,g2,g3,g4]

    for i in range(len(g)):
        x[i+1] = g[i]