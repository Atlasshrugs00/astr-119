import numpy as np

i = 10
print(type(i)) #prints data type of i

a_i = np.zeros(i,dtype=int) #declares array of integers
print(type(a_i)) #will return ndarray
print(type(a_i[0])) #will return int64

x = 119.0
print(type(x)) #prints out data type of x

y = 1.19e2
print(type(y)) #print out data type of y

z = np.zeros(i,dtype=float) #declares array of floats
print(type(z))
print(type(z[0]))