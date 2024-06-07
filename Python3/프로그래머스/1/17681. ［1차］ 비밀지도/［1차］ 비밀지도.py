
from collections import deque
def solution(n, arr1, arr2):
    answer = []
    answer_list = []
    for i in range(n):
        arr1_list = deque()
        for j in range(n):
            check_num = int(arr1[i]%2)+int(arr2[i]%2)
            if check_num > 0 : 
                check_str = "#"
            else:
                check_str = " "
            arr1_list.appendleft(check_str)
            arr1[i]=int(arr1[i]/2)
            arr2[i]=int(arr2[i]/2)
        answer_list.append(arr1_list)
    for i in range(n):
        answer_str = ""
        for j in range(n):
            answer_str += answer_list[i][j]
        answer.append(answer_str)    
    return answer