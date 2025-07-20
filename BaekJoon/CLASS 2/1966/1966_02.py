import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, target = map(int, input().split())
    task_queue = list(map(int, input().split()))

    cnt = 0

    while task_queue:
        if target < 0:
            break

        max_priority = max(task_queue)

        if task_queue[0] == max_priority:
            task_queue.pop(0)
            cnt += 1
            target -= 1
        else:
            tmp = task_queue.pop(0)
            task_queue.append(tmp)

            if target == 0:
                target = len(task_queue) - 1
                continue

            target -= 1
            
    
    print(cnt)    