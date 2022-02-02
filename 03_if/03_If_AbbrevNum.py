n = int(input())

if n >= 10000000000:
    print(str(int(round(n/1000000000, 0))) + 'B')
elif n >= 1000000000:
    print(str(round(n/1000000000, 1)) + 'B')
elif n >= 10000000:
    print(str(int(round(n/1000000, 0))) + 'M')
elif n >= 1000000:
    print(str(round(n/1000000, 1)) + 'M')
elif n >= 10000:
    print(str(int(round(n/1000, 0))) + 'K')
elif n >= 1000:
    print(str(round(n/1000, 1)) + 'K')
else:
    print(n)