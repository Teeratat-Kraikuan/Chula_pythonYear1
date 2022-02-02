s1 = input().split()
s2 = input().split()

s1 += [False]
s2 += [False]

if s1[2] == 'A' and s1[3] in 'ABC' and s1[4] in 'ABC':
    s1[5] = True
if s2[2] == 'A' and s2[3] in 'ABC' and s2[4] in 'ABC':
    s2[5] = True
    
if s1[5] and s2[5]:
    if float(s1[1]) > float(s2[1]):
        print(s1[0])
    elif float(s1[1]) < float(s2[1]):
        print(s2[0])
    elif s1[3] < s2[3]:
        print(s1[0])
    elif s1[3] > s2[3]:
        print(s2[0])
    elif s1[4] < s2[4]:
        print(s1[0])
    elif s1[4] > s2[4]:
        print(s2[0])
    else:
        print("Both")
elif s1[5]:
    print(s1[0])
elif s2[5]:
    print(s2[0])
else:
    print("None")