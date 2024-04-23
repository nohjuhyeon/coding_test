def solution(number):
    list_index = []
    list_number = []
    list_answer = []
    for i in range(len(number)):
        list_index.append(i)
        numbers = [i]
        list_number.append(numbers)        
    pass
    for m in range(2):
        list_answer=[]    
        for i in range(len(list_number)):
            a = list_index.index(list_number[i][-1])+1
            for j in list_index[a:]:
                second_list=[]
                for k in range(len(list_number[i])):
                    second_list.append(list_number[i][k])
                pass
                second_list.append(j)
                pass
                list_answer.append(second_list)
                pass
        list_number=[]
        for i in range(len(list_answer)):
            list_number.append(list_answer[i])
        pass
    answer = 0
    for i in range(len(list_answer)):
        sum = number[list_answer[i][0]] + number[list_answer[i][1]]+number[list_answer[i][2]]
        if sum == 0:
            answer += 1
    return answer