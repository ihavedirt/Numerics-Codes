import math as m

#composite trapezoidal rule
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
sum = 0

print('TRAPEZOIDAL')

fa = function(a)
print('\nf(a): ' +str(round(fa,decimal)))

for i in range(1,int(n)):
    x0 = a+i*h
    print('x_k: ' + str(x0))
    val = function(x0)
    print('eval: ' +str(round(val,decimal)))
    sum += val

fb = function(b)
print('\nf(b): ' +str(round(fb,decimal)))

result = h/2*(fa + 2*sum + fb)

print('\nresult: ' + str(round(result,decimal)))
