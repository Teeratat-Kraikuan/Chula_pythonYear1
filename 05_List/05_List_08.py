def gradeup(n):
    grade = ['F', 'D', 'D+', 'C', 'C+', 'B' ,'B+', 'A']
    return (grade[grade.index(n) + 1])

std = []

while True:
    s = input()
    if s == 'q':
        break
    std.append(s.split())
    
std.sort()

uids = input().split()

for i in range(len(std)):
    if std[i][0] in uids:
        std[i][1] = gradeup(std[i][1])
    print(std[i][0], std[i][1])