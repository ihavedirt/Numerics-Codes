import math as m
import copy as c
#insert parameters#######################
def function(x):
    return 1/2*m.sqrt(x**3+6)

a = float(1)
b = float(2)
tol = 10**(-5)
#########################################

decimal = 6
play = True
k = 1
err = 0
g = (b-a)/2

lst = [['k','g','diff']]

while play:

    if k > 1:
        err = abs(gPrev - g)
        if err < tol or k > 40:
            play = False

    lst.append([k,round(g,decimal),round(err,decimal)])
    # lst.append([k,g,err])

    gPrev = c.deepcopy(g)

    g = function(g)

    k += 1

for row in lst:
    print("{: >4} {: >10} {: >10}".format(*row))
