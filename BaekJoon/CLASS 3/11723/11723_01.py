import sys

input = sys.stdin.readline

def solution(command):
    global stack

    if len(command) == 2:
        command, num = command[0], int(command[1])

        if command == "add":
            stack.add(num)
        elif command == "remove":
            if num in stack:
                stack.remove(num)
        elif command == "check":
            if num in stack:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if num in stack:
                stack.remove(num)
            else:
                stack.add(num)
    else:
        if command[0] == "all":
            stack = set(i for i in range(1, 21))
        elif command[0] == "empty":
            stack = set()

T = int(input())
stack = set()

for _ in range(T):
    command = list(map(str, input().split()))

    solution(command)