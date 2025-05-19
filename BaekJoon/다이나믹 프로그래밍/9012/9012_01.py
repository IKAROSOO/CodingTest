N = int(input())

for _ in range(N):
    sentence = input()
    cnt = 0

    for word in sentence:
        if word == "(":
            cnt += 1
        elif word == ")":
            cnt -= 1

        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")