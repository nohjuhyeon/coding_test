def solution(s):
    answer_list = s.split()
    answer_lists = []
    for i in answer_list:
        answer_lists.append(int(i))
    answer = str(min(answer_lists)) + ' ' + str(max(answer_lists))
    return answer