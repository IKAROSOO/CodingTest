while True:
    str_n = input()
    length = len(str_n)

    if not int(str_n):
        break

    for i in range(length//2):
        if str_n[i] != str_n[length - i - 1]:
            print("no")
            break
    else:
        print("yes")