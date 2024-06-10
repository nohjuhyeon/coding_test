def solution(A,B):
    B = sorted(B)
    A = sorted(A,reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer