N = int(input())
shirt_list = list(map(int, input().split(" ")))
shirt_sell, pen_sell = map(int, input().split(" "))

shirt_cnt = 0

for shirt in shirt_list:
    if shirt%shirt_sell == 0:
        shirt_cnt += shirt // shirt_sell
    else:
        shirt_cnt += shirt // shirt_sell + 1

pen_cnt = list()
pen_cnt.append(N//pen_sell)
pen_cnt.append(N%pen_sell)

print(shirt_cnt)
print(pen_cnt[0], pen_cnt[1])