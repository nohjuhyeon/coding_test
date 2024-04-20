def solution(n):
    a = int(n**(1/2))
    if a**2 == n:
        answer = int((a + 1)**2)
    else:
        answer = -1
    return answer