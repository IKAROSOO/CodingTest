def solution(a, b):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    total_days = sum(month_days[0:a-1]) + b
    return days[(total_days - 1) % 7]