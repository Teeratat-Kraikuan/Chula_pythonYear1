import math
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(y):
    return ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)

def day_of_year(d, m, y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        num_of_days[1] = 29
    
    for i in num_of_days[:(m - 1)]:
        d += i
    num_of_days[1] = 28
    
    return (d)

def count_days(d1, m1, y1, d2, m2, y2):
    if is_leap_year(y1):
        num_of_days[1] = 29
    n1 = num_of_days[m1 - 1] - d1 + 1
    for i in range(m1, 12):
        n1 += num_of_days[i]
    num_of_days[1] = 28
    
    if is_leap_year(y2):
        num_of_days[1] = 29
    n2 = d2 - 1
    for i in range(0, m2 - 1):
        n2 += num_of_days[i]
    num_of_days[1] = 28
    
    return n2 + n1
        

bd, bm, by, d, m, y = [int(i) for i in input().split()]

# convert Buddhist to Christian
by -= 543
y -= 543

if by != y:
    t = count_days(bd, bm, by, d, m, y)
else:
    t = day_of_year(d, m, y) - day_of_year(bd, bm, by)
    
for i in range(by + 1, y):
    t += 365
    
phys = math.sin(2*math.pi*t/23)
emo = math.sin(2*math.pi*t/28)
intel = math.sin(2*math.pi*t/33)
print(f"{t} {phys:.2f} {emo:.2f} {intel:.2f}")