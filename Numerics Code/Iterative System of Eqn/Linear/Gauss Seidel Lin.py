import math as m

count = 0

#insert starting x##################
#insert eqns(add/sub iteration and returns) add eqn after return
def g(x,iteration):
    if iteration == 0:
        return 1/10*x[2] - 1/5*x[3] + 3/5
    elif iteration == 1:
        return 1/11*x[1] + 1/11*x[3] - 3/11*x[4] + 25/11
    elif iteration == 2:
        return -1/5*x[1] + 1/10*x[2] + 1/10*x[4]-11/10
    elif iteration == 3:
       return -3/8*x[2] + 1/8*x[3] + 15/8

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
    