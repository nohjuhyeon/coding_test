def solution(num):
    answer = 0
    x = 0
    while  x < 500:
        x = x + 1
        if num == 1:
            break
        elif num%2 == 0:
            num = int(num/2)
        else: 
            num = int(num*3 + 1)
        answer += 1
        pass
    pass
    if num != 1:
        answer = -1
    
    return answer
