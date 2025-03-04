def solution(A, B):
    answer = 0
    shifted = ""

    if A == B:
        return answer
    
    while True:
        answer += 1
        shifted = A[len(A)-answer : ] + A[: len(A)-answer]
        print(answer, shifted)

        if shifted == B:
            return answer
        if answer == len(B):
            return -1