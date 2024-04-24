def solution(k, score):
    answer = []
    answer_list = []
    for i in range(len(score)):
        answer_list.append(score[i])
        answer_list.sort(reverse=True)
        answer_list = answer_list[:k]
        answer.append(min(answer_list))
    return answer