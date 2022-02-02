min_x = 1e9
max_x = -1e9
min_y = 1e9
max_y = -1e9
i = 0
while True:
    s = input()
    if s == "Zig-Zag" or s == "Zag-Zig":
        break
    a, b = map(int, s.split())
    if i % 2:
        if min_x > b:
            min_x = b
        if max_x < b:
            max_x = b
        if min_y > a:
            min_y = a
        if max_y < a:
            max_y = a
    else:
        if min_x > a:
            min_x = a
        if max_x < a:
            max_x = a
        if min_y > b:
            min_y = b
        if max_y < b:
            max_y = b
    i += 1

if s == "Zig-Zag":
    print(min_x, max_y)
elif s == "Zag-Zig":
    print(min_y, max_x)

