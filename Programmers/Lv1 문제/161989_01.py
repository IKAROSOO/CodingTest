def solution(n, m, section):
    cnt = 0

    wall = [1]*n
    for i in section:
        wall[i-1] = 0

    for i in range(0, n-m+1, m):
        if 0 in wall[i:i+m]:
            cnt += 1
            continue
    
    if 0 in wall[-(n%m):] and n%m != 0:
        cnt += 1

    return cnt

'''
n = 10  # 벽의 길이
m = 3   # 롤러의 길이
section = [1, 5, 6, 9, 10]  # 페인트칠해야 하는 구역

위와 같은 반례가 존재
'''