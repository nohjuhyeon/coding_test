def solution(clothes):
    clothes_list = []
    for i in clothes:
        clothes_list.append(i[1])
    clothes_set = list(set(clothes_list))
    answer_list = []
    answer = 1
    for i in clothes_set:
        answer *= clothes_list.count(i)+1
    answer -= 1
    return answer