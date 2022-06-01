import math as m

#insert parameters#######################
def f(x):
    return m.cos(x)

x = float()
h = float()
#########################################

result = (f(x+h) - f(x))/h

print(result)