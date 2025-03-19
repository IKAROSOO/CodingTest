def solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_day = today.split(".")
    today_year, today_month, today_day = int(today_year), int(today_month), int(today_day)

    term_dict = {}

    for element in terms:
        kind, period = element.split(" ")
        if kind not in term_dict:
            term_dict[kind] = period
        
    for i, element in enumerate(privacies):
        date, contract = element.split(" ")
        year, month, day = date.split(".")
        year, month, day = int(year), int(month), int(day)

        month += int(term_dict[contract])
        
        day -= 1
        if day == 0:
            day = 28
            month -=1

        while month > 12:
            month -= 12
            year += 1
        
        print(year, month, day, i)
        
        if year > today_year:
            continue
        elif year < today_year:
            answer.append(i+1)
        else:
            if month > today_month:
                continue
            elif month < today_month:
                answer.append(i+1)
            else:
                if day >= today_day:
                    continue
                else:
                    answer.append(i+1)
        
        print(year, month, day, i)
        
    return answer