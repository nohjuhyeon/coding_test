def solution(s):
    answer = s[0].upper()
    check = s[0]
    for i in range(1,len(s)):
        if check == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        check = s[i]
    return answer