s = input()

cnt = 0
s_sum = 0
while s != 'q':
    s_sum += float(s)
    cnt += 1
    s = input()
    
if s_sum == 0:
    print("No Data")
else:
    print(round(s_sum / cnt, 2))