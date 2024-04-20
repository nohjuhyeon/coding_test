def solution(n):
    list_n = list(str(n))
    for i in range(len(list_n)):
        list_n[i] = int(list_n[i])
    list_n.sort(reverse=True)
    answer = ""
    for i in range(len(list_n)):
        list_n[i] = str(list_n[i])
        answer = answer+list_n[i]
    answer = int(answer)
    return answer