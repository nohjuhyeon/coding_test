def solution(n):
    answer_list = [1,2]
    if n <= 2:
        answer = answer_list[n-1]
    else:
        for i in range(n-2):
            answer_list.append(answer_list[-1]+answer_list[-2])
        answer = answer_list[-1]
    return answer%1234567