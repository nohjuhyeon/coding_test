def solution(s, n):
    list_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list_lower = []
    for i in range(len(list_upper)):
        list_lower.append(list_upper[i].lower())
    pass
    answer = ''
    for i in range(len(s)):
        if s[i] in list_upper:
            index = list_upper.index(s[i])
            answer = answer + list_upper[int((index + n)%len(list_upper))]
        elif s[i] in list_lower:
            index = list_lower.index(s[i])
            answer = answer + list_lower[int((index + n)%len(list_lower))]
        else:
            answer = answer + s[i]
    return answer
