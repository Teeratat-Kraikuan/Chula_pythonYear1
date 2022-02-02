num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = int(input())
m = int(input())
y = int(input())

y -= 543
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    num_of_days[1] = 29
    
for i in num_of_days[:(m - 1)]:
    d += i
    
print(d)