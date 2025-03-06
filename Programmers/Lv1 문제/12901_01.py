def solution(a, b):
    cnt = 0

    month = {
        "1" : 31,
        "2" : 29,
        "3" : 31,
        "4" : 30,
        "5" : 31,
        "6" : 30,
        "7" : 31,
        "8" : 31,
        "9" : 30,
        "10" : 31,
        "11" : 30,
        "12" : 31
    }
    day = {
        0 : "FRI",
        1 : "SAT",
        2 : "SUN",
        3 : "MON",
        4 : "TUE",
        5 : "WED",
        6 : "THR"
    }

    a -= 1
    while a != 0:
        cnt += month[str(a)]
        a -= 1
    cnt += b-1

    return day[cnt%7]