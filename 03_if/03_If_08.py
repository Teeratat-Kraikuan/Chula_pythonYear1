n = int(input())

if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
    
if n % 2:
    print("odd")
else:
    print("even")