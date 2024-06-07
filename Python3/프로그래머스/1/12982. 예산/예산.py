def solution(d, budget):
    d.sort()
    sum_d = sum(d)
    answer = 0
    for i in range(len(d)):
        if sum_d <= budget:
            answer = len(d)-i
            break
        else:
            sum_d = sum_d - d[-i-1]
            pass
        pass
    return answer