from math import gcd
s = input().split(',')

s1 = s[0]
s2 = '0' + s[1]
s3 = s[2]

n1 = int(s2+s3) - int(s2)
n2 = int(len(s3)*'9' + (len(s2)-1)*'0')

print((n1+int(s1)*n2)//gcd(n1,n2), '/', n2//gcd(n1,n2))
