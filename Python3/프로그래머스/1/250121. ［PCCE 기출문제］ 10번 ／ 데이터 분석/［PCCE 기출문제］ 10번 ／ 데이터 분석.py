
def solution(data, ext, val_ext, sort_by):
    list_criteria = ['code','date','maximum','remain']
    list_data = []
    for i in data:
        data_dict = {list_criteria[0]:i[0],list_criteria[1]:i[1],list_criteria[2]:i[2],list_criteria[3]:i[3]}
        list_data.append(data_dict)
    sort_index = list_criteria.index(sort_by)
    answer_list = []
    for i in list_data:
        if i[ext] < val_ext:
            answer_list.append(i)

    sort_list = sorted(answer_list,key=lambda i:(i[sort_by]))
    answer = []
    for i in sort_list:
        answer_list = i.values()
        answer.append(list(answer_list))
    return answer