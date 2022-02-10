import math
a = float(input())
b = float(input())
c = float(input())

degree = math.degrees(math.acos((0.5*((a-b) + (a-c))) / (((a-b)**2 + (a-c)*(b-c))**0.5)))

print(int(360 - degree))