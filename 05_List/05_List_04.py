n = [int(i) for i in input().split()]

ans = 0
for i in range(1, len(n)-1):
    if n[i-1] < n[i] > n[i+1]:
       ans += 1
       
print(ans)