def solution(s):
    check = 0
    answer = True
    for i in s:
        if i == '(':
            check += 1
        else:
            if check == 0:
                answer = False
                break
            else:
                check -= 1    
    if check != 0:
        answer = False
    return answer