while True:
    try:
        n = int(input())
    except:
        break

    answer = 1
    i = 1

    while answer%n != 0:
        answer += 10**i
        i += 1
    
    print(i)