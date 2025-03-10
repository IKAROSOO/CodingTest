'''주어진 가로 길이 n과 세로 길이 m을 사용하여
별(*) 문자로 직사각형을 출력하는 문제'''

a, b = map(int, input().split())

for _ in range(b):
    print("*"*a)