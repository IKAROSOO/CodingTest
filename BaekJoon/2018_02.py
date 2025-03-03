N = int(input())

num = [i+1 for i in range(N)]

start_index, end_index = 0, 0
sum = 1
cnt = 1

while end_index != N-1:
    if sum == N:
        cnt += 1
        end_index += 1
        sum += num[end_index]
    elif sum > N:
        sum -= num[start_index]
        start_index += 1
    elif sum < N:
        end_index += 1
        sum += num[end_index]
    
print(cnt)