N = int(input())

digits = 1
count = 0
while 10**digits - 1 < N:
    # 각 자릿수 범위의 숫자 개수 * 자릿수
    count += (10**digits - 10**(digits - 1)) * digits
    digits += 1

# 마지막 자릿수 범위에서 남은 숫자들의 자릿수 더하기
count += (N - 10**(digits - 1) + 1) * digits

print(count)
