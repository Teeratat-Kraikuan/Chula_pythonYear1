s = [float(i) for i in input().split()]
# print(round((sum(s)-max(s)-min(s)) / 2, 2))

mx = 0
mn = 1e9
var_sum = 0

for i in s:
    if mx < i:
        mx = i
    if mn > i:
        mn = i
    var_sum += i

print(round((var_sum - mx - mn) / 2, 2))