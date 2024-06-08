n = int(input())

def question(n):
    list_answer = ['666']
    list_answer_num = [666]
    while True:
        list_answer_element=[]
        list_answer_element_num=[]
        for i in range(len(list_answer)):
            for j in range(10):
                list_answer_element.append(list_answer[i]+str(j))
                list_answer_element.append(str(j)+list_answer[i])
                list_answer_element_num.append(int(list_answer[i]+str(j)))
                list_answer_element_num.append(int(str(j)+list_answer[i]))
        list_answer.extend(list_answer_element)
        list_answer_num.extend(list_answer_element_num)
        list_answer_num = list(sorted(set(list_answer_num)))
        if len(list_answer_num) > n:
            answer = list_answer_num[n-1]
            break
    return  answer

answer = question(n)
print(answer)