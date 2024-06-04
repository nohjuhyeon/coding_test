def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        answer_num = 0
        for j in targets[i]:
            check_num = []
            for k in keymap:
                if j in k:
                    check_num.append(k.find(j)+1)
                    pass
            if len(check_num) != 0:
                answer_num += min(check_num)
            else:
                answer_num = -1
                break
        answer.append(answer_num)
    return answer