T = int(input())
calender = []

for i in range(T):
    data = list(map(int, input().split()))
    calender.append(data)

for datas in calender:
    cnt = 1 
    x, y = 1, 1 
    for i in range(datas[0]*datas[1]):      
        if x == datas[2] and y == datas[3]:
            print(cnt)
            break

        if x < datas[0]:
            x += 1
        else:
            x = 1
        
        if y < datas[1]:
            y += 1
        else:
            y = 1
        
        cnt += 1

        if i == datas[0]*datas[1] - 1:
            print(-1)