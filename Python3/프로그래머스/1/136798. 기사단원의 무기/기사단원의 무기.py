def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        answer_num = []
        repeat = int(i**0.5)+1
        for j in range(1,repeat+1):
            if i%j == 0:
                answer_num.append(j)
                answer_num.append(int(i/j))
        answer_num = len(set(answer_num))
        if answer_num <= limit:
            answer += answer_num
        else:
            answer += power
    return answer
