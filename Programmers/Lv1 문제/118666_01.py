def solution(surveys, choices):
    answer = ""

    personallity_dict = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0
    }
    
    for survey, choice in zip(surveys, choices):
        left, right = survey[0], survey[1]

        if choice == 4:
            continue
        else:
            if choice > 4:
                personallity_dict[right] += choice-4
            else:
                personallity_dict[left] += 4-choice

    if personallity_dict["R"] >= personallity_dict["T"]:
        answer += "R"
    else:
        answer += "T"
    
    if personallity_dict["C"] >= personallity_dict["F"]:
        answer += "C"
    else:
        answer += "F"

    if personallity_dict["J"] >= personallity_dict["M"]:
        answer += "J"
    else:
        answer += "M"
    
    if personallity_dict["A"] >= personallity_dict["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer