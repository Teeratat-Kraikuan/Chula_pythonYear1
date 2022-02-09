name = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anothony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

n = int(input())

ans = []
for i in range(n):
    s = input()
    ans.append(s)
    
for i in ans:
    if i in name:
        print(nickname[name.index(i)])
    elif i in nickname:
        print(name[nickname.index(i)])
    else:
        print("Not found")