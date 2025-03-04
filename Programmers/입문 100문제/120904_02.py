def solution(num, k):
    num = str(num)
    k = str(k)

    try:
        return num.index(k) + 1
    except:
        return -1