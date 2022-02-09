lst = ['0','1','2','3','4','5','6','7','8','9']

s = list(input())

for i in s:
    if i in lst:
        lst.remove(i)

if lst:
    print(','.join(lst))
else:
    print("None")