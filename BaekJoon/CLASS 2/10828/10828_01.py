import sys

input = sys.stdin.readline

def solution(order_list, stack):
    if len(order_list) == 1:
        order = order_list[0]

        if order == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif order == "size":
            print(len(stack))
        elif order == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif order == "pop":
            if stack:
                n = stack.pop()
                print(n)
            else:
                print(-1)
    else:
        order, num = order_list

        if order == "push":
            stack.append(int(num))

n = int(input())
stack = []

for _ in range(n):
    order_list = input().split()

    solution(order_list, stack)