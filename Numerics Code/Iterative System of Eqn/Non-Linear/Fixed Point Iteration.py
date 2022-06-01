import math as m

count = 0

#insert starting x##################

#starting x vals
x = [count,1.0,-1.0,1.0]

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
    g1 = m.sqrt(16 + 9*x[1]*x[2] - x[2]*x[3])
    g2 = 6 / (8*x[1] + x[2] + 3*x[3])
    g3 = m.sqrt(6*x[1] + 3*x[2]*x[3] + 21)

    g = [g1,g2,g3]

    for i in range(len(x)-1):
        x[i+1] = g[i]