while True:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break

    a, b = 1, 2

    print(f"{n} = {a} + {b}")