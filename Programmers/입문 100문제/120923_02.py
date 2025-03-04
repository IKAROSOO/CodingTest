def solution(num, total):
    midNum = total//num
    startNum = midNum - ((num-1)//2)
    print(midNum, startNum)

    return list(range(startNum, startNum + num))