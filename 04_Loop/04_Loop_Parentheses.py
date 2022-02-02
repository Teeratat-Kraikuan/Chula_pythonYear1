s = list(input())

l = len(s)

for i in range(l):
    if s[i] == '(':
        s[i] = '['
    elif s[i] == '[':
        s[i] = '('
    elif s[i] == ')':
        s[i] = ']'
    elif s[i] == ']':
        s[i] = ')' 

print(''.join(s))