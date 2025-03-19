def to_days(date):
    year, month, day = map(int, date.split("."))
    return year*28*12 + month*28 + day

def solution(today, terms, privacies):
    answer = []
    months = {}

    for term in terms:
        key, value = term.split()
        months[key] = int(value)*28
    
    today_days = to_days(today)
    
    for i, privacy in enumerate(privacies):
        privacy_date, term_type = privacy.split()
        privacy_days = to_days(privacy_date)

        if privacy_days + months[term_type] <= today_days:
            answer.append(i+1)
    
    return answer