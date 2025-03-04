def solution(num, k):
    num = str(num)

    try:
        return num.index(f"{k}") + 1
    except:
        return -1