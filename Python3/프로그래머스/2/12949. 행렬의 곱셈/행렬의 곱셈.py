def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer_list = []    
        for j in range(len(arr2[0])):
            answer_num = 0
            for k in range(len(arr2)):
                answer_num += arr1[i][k]*arr2[k][j]
            answer_list.append(answer_num)
        answer.append(answer_list)
    return answer