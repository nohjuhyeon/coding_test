def solution(ingredient):
    answer_list = []
    answer = 0
    for i in ingredient:
        if len(answer_list) != 0:
            if answer_list[-1] == 1:
                if i == 1:
                    answer_list.append(i)
                elif i == 2:
                    answer_list[-1] += 2
                else:
                    answer_list= []
            elif answer_list[-1] == 3:
                if i == 1:
                    answer_list.append(i)
                elif i == 3:
                    answer_list[-1] += 3
                else:
                    answer_list= []
            elif answer_list[-1] == 6:
                if i == 1:
                    answer += 1
                    answer_list= answer_list[:-1]
                else:
                    answer_list = []
        else:
            if i == 1:
                answer_list.append(i)
    return answer