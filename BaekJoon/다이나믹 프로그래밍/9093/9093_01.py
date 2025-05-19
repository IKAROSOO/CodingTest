N = int(input())
sentences = list()

for _ in range(N):
    sentences.append(input())

for sentence in sentences:
    answer = ""
    for word in sentence:
        answer += word[::-1] + " "
    print(answer.strip())