from math import log
w = float(input())
h = float(input())
Mosteller = ((w*h)**(1/2))/60
Haycock = 0.024265 * w**0.5378 * h**0.3964
Boyd = 0.0333 * w**(0.6157-0.0188*log(w,10)) * h**0.3
print(Mosteller)
print(Haycock)
print(Boyd)