n = int(input())

lst = []

for i in range(n):
    x = int(input())
    lst.append(x)
    
x = [int(i) for i in input().split()]
for i in x:
    lst.append(i)
    
x = int(input())
while x != -1:
    lst.append(x)
    x = int(input())

ans = []
for i in range(len(lst)):
    if i % 2:
        ans.insert(0, lst[i])
    else:
        ans.append(lst[i])
        
print(ans)