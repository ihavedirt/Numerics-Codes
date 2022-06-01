#diff from example answer, might be rounding error on their part
import math as m
import copy as c
#insert parameters#######################
def function(x):
    return x**3-3*x**2+2*x*m.sin(x) + 11

a = float(-3)
b = float(3)
tol = 10**(-5)
decimal = 6
#########################################

play = True
k = 1
p = (a+b)/2
err = 0
aResult = function(a)
pResult = function(p)
bResult = function(b)

lst = [['k','a','p','b','aResult','pResult','bResult','diff']]

while play:
    p = a+(b-a)/2
    lst.append([k,round(a,decimal),round(p,decimal),round(b,decimal),round(aResult,decimal),round(pResult,decimal),round(bResult,decimal),round(err,decimal+2)])

    if k > 1:
        err = abs(pPrev - p)
        if err < tol:
            play = False

    aResult = function(a)

    pResult = function(p)

    bResult = function(b)

    if aResult*pResult > 0:
        a = p
    else:
        b = p

    pPrev = c.deepcopy(p)

    k += 1

for row in lst:
    print("{: >4} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10}".format(*row))