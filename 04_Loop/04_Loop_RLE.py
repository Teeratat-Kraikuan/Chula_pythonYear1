s = input()

t = s[0]
cnt = 0
for c in s:
    if t == c:
        cnt += 1
    else:
        print(t, cnt, end=" ")
        t = c
        cnt = 1
print(t, cnt)