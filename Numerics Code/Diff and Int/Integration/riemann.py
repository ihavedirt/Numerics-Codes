import math as m


#insert parameters
b = 3.0
a = 2.0
subint = 10.0
decimal = 4

def function(x):
    return x**2*m.exp(-m.cos(x))

    

def left(a,x,iteration):
    deltaX = a+x*iteration
    print('deltaX: ' + str(deltaX))
    return function(deltaX)

def right(a,x,iteration):
    deltaX = a+x*iteration
    print('deltaX: ' + str(deltaX))
    return function(deltaX)

def mid(a,x,iteration):
    deltaX = a+(2*iteration-1)*(x/2)
    print('deltaX: ' + str(deltaX))
    return function(deltaX)

x = (b-a)/subint

print('LEFT')
sum = 0

for i in range(int(subint)):
    val = left(a,x,i)
    print('eval: ' + str(round(val, decimal)))
    sum += val

print('final result ' + str(round(sum*x,decimal)))



print('\nRIGHT')
sum = 0

for i in range(1,int(subint) + 1):
    val = right(a,x,i)
    print('eval: ' + str(round(val,decimal)))
    sum += val

print('final result ' + str(round(sum*x,decimal)))



print('\nMIDPOINT')
sum = 0

for i in range(1,int(subint) + 1):
    val = mid(a,x,i)
    print('eval: ' + str(round(val,decimal)))
    sum += val

print('final result ' + str(round(sum*x,decimal)))