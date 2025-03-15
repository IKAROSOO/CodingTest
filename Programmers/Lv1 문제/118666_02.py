def solution(surveys, choices):
    answer = ""

    personality_dict = {
        "R" : 0, "T" : 0, "C" : 0, "F" : 0,
        "J" : 0, "M" : 0, "A" : 0, "N" : 0
    }
    
    for survey, choice in zip(surveys, choices):
        left, right = survey[0], survey[1]

        if choice == 4:
            continue
        else:
            if choice > 4:
                personality_dict[right] += choice-4
            else:
                personality_dict[left] += 4-choice
    
    personality_groups = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]

    for group in personality_groups:
        if personality_dict[group[0]] >= personality_dict[group[1]]:
            answer += group[0]
        else:
            answer += group[1]
    
    return answer