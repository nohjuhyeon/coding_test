def solution(s):
    list_s = []
    for i in s:
        if len(list_s) == 0:
            list_s.append(i)
        elif i == list_s[-1]:
            list_s.pop(-1)
        else:
            list_s.append(i)
    if len(list_s) == 0:
        answer = 1
    else:
        answer = 0
    return answer
