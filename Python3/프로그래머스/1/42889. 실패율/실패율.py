from collections import deque

def solution(N, stages):
    dict_answer = {}
    stages.sort()
    stages = deque(stages)
    for i in range(N):
        entire_num = len(stages)
        if entire_num == 0:
            dict_answer[i+1] = 0
        else:
            fail_num = 0
            for j in range(len(stages)):
                if stages[0] <= i+1:
                    stages.popleft()
                    fail_num +=1
                else:
                    break
            dict_answer[i+1] = (fail_num/entire_num)
    answer_list = sorted(dict_answer.items(), key=lambda x: (-x[1]))
    answer = [0]*N
    for i in range(N):
        answer[i] = answer_list[i][0]
    return answer
