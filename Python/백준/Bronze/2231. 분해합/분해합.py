N = int(input())

def question(N):
    answer_list = []
    for i in range(1,N+1):
        str_i = str(i)
        str_i_sum = 0
        for j in range(len(str_i)):
            str_i_sum += int(str_i[j])
        if i+str_i_sum == N:
            answer_list.append(i)
    if len(answer_list) == 0:
        answer = 0
    else:
        answer = min(answer_list)
    return answer

answer = question(N)
print(answer)