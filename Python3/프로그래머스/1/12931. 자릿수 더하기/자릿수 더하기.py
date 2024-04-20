def solution(n):
    list_n = list(str(n))
    answer = 0
    for i in range(len(list_n)):
        answer += int(list_n[i])
    return answer
