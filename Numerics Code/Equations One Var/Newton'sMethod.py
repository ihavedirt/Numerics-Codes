import math as m
import copy as c
#insert parameters#######################
def function(x):
    return x**3 + 4*x**2 - 10

def functionDiff(x):
    return 3*x**2 + 8*x

p = float(1)
tol = 10**(-5)
#########################################

decimal = 6
play = True
k = 1
err = 0

lst = [['k','p','fp',"f'p",'error']]

while play:

    if k > 1:
        err = abs(pPrev - p)
        if err < tol or k > 40:
            play = False

    fdp = functionDiff(p)
    fp = function(p)

    lst.append([k,round(p,decimal),round(fp,decimal),round(fdp,decimal),round(err,decimal)])

    pPrev = c.deepcopy(p)

    p = p - fp/fdp

    k += 1

for row in lst:
    print("{: >4} {: >10} {: >10} {: >10} {: >10}".format(*row))
