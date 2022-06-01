import math as m

#composite sumpsons rule
#parameters#########################
b = 3.0
a = 2.0
n = 10.0
decimal = 3

def function(x):
    return x**2*m.exp(-m.cos((x)))
#####################################

#calculations
h = (b-a)/n
sum1 = 0
sum2 = 0

print('\nSIMPSONS')

fa = function(a)
print('\nf(a): ' +str(round(fa,decimal)))

print('\ntimes 2 part')
for i in range(1,int(n/2)):
    x0 = a+2*i*h
    print('x_k: ' + str(x0))
    val = function(x0)
    print('eval: ' + str(round(val, decimal)))
    sum1 += val

print('\ntimes 4 part')
for i in range(1,int(n/2)+1):
    x0 = a+(2*i-1)*h
    print('x_k: ' + str(x0))
    val = function(x0)
    print('eval: ' + str(round(val, decimal)))
    sum2 += val

fb = function(b)
print('\nf(b): ' +str(round(fb,decimal)))

result = h/3*(fa + 2*sum1 + 4*sum2 + fb)

print('\nresult: ' + str(round(result,decimal)))

