def solution(n):
    answer = 0
    for i in range(n):
        if (n%(i+1) == 0 and (i+1)%2 == 1) or (n%(i+1)/(i+1) == 0.5 and (i+1)%2== 0):
            if (n/(i+1))*2 - (i+1) < 1:
                break
            else:
                answer += 1
    return answer
