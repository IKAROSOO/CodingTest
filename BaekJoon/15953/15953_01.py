def prize_2017(grade):
    if grade == 1:
        return 5000000
    elif grade <= 3 and grade >= 2:
        return 3000000
    elif grade <= 6 and grade >= 4:
        return 2000000
    elif grade <= 10 and grade >= 7:
        return 500000
    elif grade <= 15 and grade >= 11:
        return 300000
    elif grade <= 21 and grade >= 16:
        return 100000
    else:
        return 0

def prize_2018(grade):
    if grade == 1:
        return 5120000
    elif grade <= 3 and grade >= 2:
        return 2560000
    elif grade <= 7 and grade >= 4:
        return 1280000
    elif grade <= 15 and grade >= 8:
        return 640000
    elif grade <= 31 and grade >= 16:
        return 320000
    else:
        return 0
    
N = int(input())

for _ in range(N):
    grade_2017, grade_2018 = map(int, input().split())
    print(prize_2017(grade_2017) + prize_2018(grade_2018))