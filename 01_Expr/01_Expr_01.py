from math import *
n = int(input())
a = sqrt(2*pi)*n**(n+0.5)*e**(-n+(1/(12*n+1)))
b = sqrt(2*pi)*n**(n+0.5)*e**(-n+(1/(12*n)))
print(a)
print(b)