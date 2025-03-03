n = int(input())
score = list(map(int, input().split()))

score_max = max(score)
sum = sum(score)

print(sum*100/score_max/n)