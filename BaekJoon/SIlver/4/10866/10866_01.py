import sys
from collections import deque

input = sys.stdin.readline

def solution(command):
    global stack

    if len(command) == 2:
        command, num = command[0], int(command[1])

        if command == "push_front":
            stack.appendleft(num)
        elif command == "push_back":
            stack.append(num)
    else:
        command = command[0]

        if command == "pop_front":
            if stack:
                answer = stack.popleft()
                print(answer)
            else:
                print(-1)
        elif command == "pop_back":
            if stack:
                answer = stack.pop()
                print(answer)
            else:
                print(-1)
        if command == "size":
            print(len(stack))
        elif command == "empty":
            if not stack:
                print(1)
            else:
                print(0)
        elif command == "front":
            if stack:
                print(stack[0])
            else:
                print(-1)
        elif command == "back":
            if stack:
                print(stack[-1])
            else:
                print(-1)

n = int(input())
stack = deque()
answers = list()

for _ in range(n):
    command = list((map(str, input().split())))

    solution(command)