def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer_list = []
        for j in range(commands[i][0]-1,commands[i][1]):
            answer_list.append(array[j])
        answer_list = sorted(answer_list)
        answer.append(answer_list[commands[i][2]-1])
    return answer