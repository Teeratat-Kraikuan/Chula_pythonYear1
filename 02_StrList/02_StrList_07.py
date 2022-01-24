i2s = ['A','B','C','D','E','F','G','H','I','J']
s = input()
s1 = s[3]+s[10]+s[17]+s[24]+s[31]
s2 = s[7]+s[12]+s[17]+s[22]+s[27]

n = int(s1)+int(s2)+10000
s3 = str(n//1000%10) + str(n//100%10) + str(n//10%10)
n = int(s3[0])+int(s3[1])+int(s3[2])
n = n%10 + 1
print(s3 + i2s[n-1])