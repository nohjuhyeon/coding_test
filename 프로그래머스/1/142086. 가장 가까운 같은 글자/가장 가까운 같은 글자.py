def solution(s):
    list_s = list(s)
    answer = []
    for i in range(len(list_s)):
        str_index = -1
        for j in range(i):
            if s[i] == s[j]:
                str_index = i-j
        answer.append(str_index)
    return answer