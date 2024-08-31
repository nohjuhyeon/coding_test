def solution(progresses, speeds):
    answer = [0]
    answer_list = []
    for i in range(len(progresses)):
        if ((100 - progresses[i])%speeds[i]) == 0:
            answer_list.append((100-progresses[i])//speeds[i])
        else:
            answer_list.append((100-progresses[i])//speeds[i]+1)
    check_int = answer_list[0]
    for i in answer_list:
        if check_int >= i:
            answer[-1] += 1
        else:
            check_int = i
            answer.append(1)
    return answer