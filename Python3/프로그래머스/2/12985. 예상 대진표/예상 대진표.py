def solution(n,a,b):
    a = a - 1
    b = b - 1
    answer = 0
    while a != b:
        a = a//2        
        b = b//2
        answer += 1 

    return answer