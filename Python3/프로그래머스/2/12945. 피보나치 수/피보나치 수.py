def solution(n):
    answer_list = [0,1]
    for i in range(n-1):
        answer_list.append(answer_list[-1]+answer_list[-2])
    answer = answer_list[-1]%1234567
    return answer