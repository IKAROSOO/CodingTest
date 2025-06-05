def solution(n):
    num_list = []

    while n > 0:
        b = n % 3
        if b == 0:
            num_list.append(4)
            n = n // 3 - 1
        else:
            num_list.append(b)
            n //= 3

    return ''.join(map(str, reversed(num_list)))
