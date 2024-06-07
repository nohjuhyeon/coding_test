def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer_list = []
        for j in range(len(arr1[i])):
            answer_list.append(arr1[i][j] + arr2[i][j])
        answer.append(answer_list)
    
    return answer