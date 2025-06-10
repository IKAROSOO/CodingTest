d, b = map(int, input().split(" "))

d_dict = dict()
answer_list = list()
cnt = 0

for _ in range(d):
    name = str(input())
    d_dict[name] = 1
    
for _ in range(b):
    name = str(input())
    
    if name in d_dict:
        cnt += 1
        answer_list.append(name)

answer_list.sort()

print(cnt)
for name in answer_list:
    print(name)