mans = []
for i in range(9):
    mans.append(int(input()))
mans.sort()

height = sum(mans)
found = False

for i in range(8):
    for j in range(i+1, 9):
        if height - (mans[i]+mans[j]) == 100:
            a, b = mans[i], mans[j]
            found = True
            break
    if found:
        break

mans.remove(a)
mans.remove(b)

for i in range(len(mans)):
    print(mans[i])