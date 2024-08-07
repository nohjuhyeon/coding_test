def solution(elements):
    answer_list = []
    element_list = [0]*len(elements)
    k = 0
    for i in range(len(elements)):
        for j in range(len(elements)):
            element_list[j] += elements[j-k]
        k += 1
        answer_list.extend(element_list)
    answer = len(list(set(answer_list)))
    return answer