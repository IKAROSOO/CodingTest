n = int(input())

stack = list()
answer = list()
i = 1

for _ in range(n):
    num = int(input())

    while i <= num:
        stack.append(i)
        i += 1
        answer.append("+")
    answer.append("-")

    if stack[-1] == num:
        stack.pop()
    else:
        flag = True

if flag:
    print("NO")
else:
    print(*answer)