def solution(n):
    list_n = list(str(n))
    answer = []
    for i in range(len(list_n)):
        answer.append(int(list_n[-i-1]))
    return answer
