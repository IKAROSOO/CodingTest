def solution(A, B):
    if A == B:
        return 0
    
    for i in range(len(A)):
        shifted = A[-i-1 :] + A[: -i-1]

        if shifted == B:
            return i+1
    
    return -1