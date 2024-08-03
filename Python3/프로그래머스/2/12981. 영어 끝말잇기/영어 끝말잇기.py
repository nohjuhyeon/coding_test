def solution(n, words):
    answer = [0,0]
    answer_list = []
    for i in range(len(words)):
        if len(answer_list) == 0:
            answer_list.append(words[i])
        elif words[i][0] == answer_list[-1][-1] and words[i] not in answer_list:
            answer_list.append(words[i])
        else:
            if int((i+1)%n) == 0:
                answer = [n,int((i+1)//n)]
            else:
                answer = [int((i+1)%n),int((i+1)//n)+1]
            break
    return answer