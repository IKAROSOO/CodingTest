student = []

for i in range(1, 31):
    student.append(i)

for i in range(28):
    num = int(input())
    student.remove(num)

for i in range(2):
    print(student[i])