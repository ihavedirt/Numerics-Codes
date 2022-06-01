import math as m
import copy as c
#insert parameters#######################
def function(x):
    return x**2 - 7*x - 13

a = float(-8)
b = float(2)
tol = 10**(-5)
#########################################

decimal = 6
play = True
k = 1
err = 0

lst = [['k','a','p','b','aResult','pResult','bResult','diff']]

while play:
    fa = function(a)
    fb = function(b)
    p = a-((b-a)*fa/(fb-fa))
    fp = function(p)

    if k > 1:
        err = abs(pPrev - p)
        if err < tol:
            play = False

    lst.append([k,round(a,decimal),round(p,decimal),round(b,decimal),round(fa,decimal),round(fp,decimal),round(fb,decimal),round(err,decimal+2)])

    if fa*fp>0:
        a = p
    else:
        b = p

    pPrev = c.deepcopy(p)

    k += 1


for row in lst:
    print("{: >4} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10}".format(*row))