import numpy as np

A = np.array([[2,-1,3,10],
              [-3,1,2,-1.5],
              [1,-4,1,7.5]])


index = []

print(A)

for normalize in range(len(A)):

    #normalize
    temp = A[normalize][normalize]
    A[normalize] = A[normalize]/temp
    


# B = np.add(A[1],A[1][0]*-1*A[0])

# A[1] = B



print(A)