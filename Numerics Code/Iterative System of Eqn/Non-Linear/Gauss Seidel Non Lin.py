import math as m

count = 0

#insert starting x##################
#insert eqns(add/sub iteration and returns) add eqn after return
def g(x,iteration):
    if iteration == 0:
        return (18-3*x[3]**2-x[2])/7
    elif iteration == 1:
        return (19+x[3]+x[1]**2)/8
    elif iteration == 2:
        return (-9+x[1]+x[2]**2)/5
    # elif iteration == 3:
    #    return 

#starting x vals
x = [count,2.17315,2.97938,0.40997]

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

    for i in range(len(x)-1):
        x[i+1] = g(x,i)



