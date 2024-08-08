def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        discount_list = discount[i:i+10]
        answer_count = 1
        for j in range(len(want)):
            if discount_list.count(want[j]) >= number[j]:
                pass
            else:
                answer_count = 0
                break
        answer += answer_count
        pass
    
    return answer