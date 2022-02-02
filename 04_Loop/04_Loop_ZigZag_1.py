n = int(input())

x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    if i % 2:
        x.append(b)
        y.append(a)
    else:
        x.append(a)
        y.append(b)

command = input()
if command == "Zig-Zag":
    print(min(x), max(y))
elif command == "Zag-Zig":
    print(min(y), max(x))
