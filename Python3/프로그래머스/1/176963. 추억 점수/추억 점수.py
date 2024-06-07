def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        answer_num = 0
        for j in range(len(name)):
            answer_num += photo[i].count(name[j])*yearning[j]
        answer.append(answer_num)
    return answer