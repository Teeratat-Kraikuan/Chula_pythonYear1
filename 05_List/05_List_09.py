lst = []
n = int(input())
for i in range(n):
    lst.append([float(i) for i in input().split()])
print(f"#{lst.index(sorted(lst)[2]) + 1}: ({sorted(lst)[2][0]}, {sorted(lst)[2][1]})")