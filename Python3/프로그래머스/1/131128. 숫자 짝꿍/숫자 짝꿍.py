def solution(X, Y):
    list_x = list(X)
    list_y = list(Y)
    answer_set = list(set(list_x).intersection(set(list_y)))
    answer_list=[]
    for i in answer_set:
        if list_x.count(i) > list_y.count(i):
            answer_list.extend([i]*(list_y.count(i)))
        else:
            answer_list.extend([i]*(list_x.count(i)))
    answer_list.sort(reverse=True)
    if len(answer_list) == 0:
        answer = '-1'
    elif list(set(answer_list)) == ['0']:
        answer = '0'
    else:
        answer = ''.join(answer_list)
    return answer
