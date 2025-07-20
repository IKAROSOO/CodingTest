while True:
    nums = list(map(int, input().split()))
    nums.sort()

    a, b, c = nums[0], nums[1], nums[2]

    if a == 0 and b == 0 and c == 0:
        break

    if (a**2 + b**2) == c**2:
        print("right")
    else:
        print("wrong")