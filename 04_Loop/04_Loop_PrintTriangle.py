n = int(input())

for i in range(n):
    if i == 0:
        print(' '*(n - i - 1) + '*')
    elif i == n - 1:
        print('*'*(n * 2 - 1))
    else:
        print(' '*(n - i - 1) + '*' + ' '*(i * 2 - 1) + '*')