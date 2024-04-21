def solution(s):
    answer = ''
    list_s = sorted(s,reverse=True)
    for i in range(len(list_s)):
        answer += list_s[i]
    return answer