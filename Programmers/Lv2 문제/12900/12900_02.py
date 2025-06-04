def solution(n):
    cnt_list = list(0 for _ in range(n))

    cnt_list[0] = 1
    # n=1인 경우
    cnt_list[1] = 2
    # n=2인 경우

    for i in range(2, n):
        cnt_list[i] = (cnt_list[i-1] + cnt_list[i-2]) % 1000000007
    
    return cnt_list[n-1]

'''
GPT가 푸는데 도움을 줌
'''