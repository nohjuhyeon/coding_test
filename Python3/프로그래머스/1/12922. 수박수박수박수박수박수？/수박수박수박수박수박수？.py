def solution(n):
    answer = ""
    if n%2 == 0:
        for i in range(int(n/2)):
            answer = answer + "수박"
    else:
        for i in range(int(n/2)):
            answer = answer + "수박"
        answer = answer + "수"
    return answer