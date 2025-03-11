def solution(answers):
    math1_pattern = [1, 2, 3, 4, 5]
    math2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    math3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]  # 각 수포자의 점수

    for index, answer in enumerate(answers):
        if answer == math1_pattern[index % len(math1_pattern)]:
            scores[0] += 1
        if answer == math2_pattern[index % len(math2_pattern)]:
            scores[1] += 1
        if answer == math3_pattern[index % len(math3_pattern)]:
            scores[2] += 1
    
    max_score = max(scores)

    return list(i+1 for i, score in enumerate(scores) if score == max_score)