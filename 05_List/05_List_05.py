n = [int(i) for i in input().split()]

ans = []

for i in n:
    if i not in ans:
        ans.append(i)
        
print(len(ans))
print(sorted(ans)[:10])
        