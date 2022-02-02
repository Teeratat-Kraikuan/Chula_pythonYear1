s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

if l1 != l2:
    print("Incomplete answer")
else:
    cnt = 0
    for i in range(l1):
        if s1[i] == s2[i]:
            cnt += 1
    print(cnt)