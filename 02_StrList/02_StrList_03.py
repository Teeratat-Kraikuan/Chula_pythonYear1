months = ["January", "February" , "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

s = input()
d, m, y = s.split('/')
print(months[int(m)-1] + ' ' + d + ', ' + y)