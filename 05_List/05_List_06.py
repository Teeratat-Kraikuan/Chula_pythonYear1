n = int(input())

ans = []
ans.append(n)
while n != 1:
    if n % 2:
        n = 3*n + 1
    else:
        n //= 2
    ans.append(n)
    
print(*ans[-15:], sep='->')