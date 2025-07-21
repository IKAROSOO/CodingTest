T = int(input())

for _ in range(T):
    n = int(input())
    clothes = dict()

    cnt = 1

    for _ in range(n):
        _, cloth_type = map(str, input().split())

        if cloth_type not in clothes:
            clothes[cloth_type] = 1
        
        clothes[cloth_type] += 1
    
    for value in clothes.values():
        cnt *= value
    
    print(cnt - 1)