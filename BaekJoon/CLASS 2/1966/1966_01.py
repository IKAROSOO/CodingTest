n = int(input())

for _ in range(n):
    amount, target = map(int, input().split(" "))

    print_list = list(map(int, input().split(" ")))

    flag = False
    cnt = 0

    while True:
        if flag:
            break

        now = print_list[0]

        if now == max(print_list):
            cnt += 1
            print_list.pop(0)
            
            if target == 0:
                flag = True
            
            target -= 1
        else:
            print_list.append(print_list[0])
            print_list.pop(0)

            if target == 0:
                target = len(print_list) - 1
            else:
                target -= 1
    
    print(cnt)

'''
2025_07_09_08:52
'''