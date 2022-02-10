months_of_years = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

d, m, y = input().split('/')

ans = '* DATE: ' + d + '.' + months_of_years[int(m)-1] + '.' + y + ' *'

print('*' * len(ans))
print(ans)
print('*' * len(ans))