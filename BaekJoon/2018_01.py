N = int(input())

start_index = 1
end_index = 1
sum = 1
cnt = 1     # 기본적으로 자기자신을 포함하기 때문에 1부터 시작한다

while end_index != N:
    if sum == N:
        cnt += 1
        end_index += 1
        sum += end_index
    elif sum > N:
        sum -= start_index
        start_index += 1
    elif sum < N:
        end_index += 1
        sum += end_index

print(cnt)