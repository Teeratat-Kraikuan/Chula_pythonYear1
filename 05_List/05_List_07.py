def gradeup(n):
    grade = ['F', 'D', 'D+', 'C', 'C+', 'B' ,'B+', 'A']
    return (grade[grade.index(n) + 1])

ids = []
grades = []

while(True):
    s = input()
    if s == 'q':
        break
    ids.append(s.split()[0])
    grades.append(s.split()[1])
    
uids = input().split()

for i in range(len(ids)):
    if ids[i] in uids:
        grades[i] = gradeup(grades[i])
    print(ids[i], grades[i])