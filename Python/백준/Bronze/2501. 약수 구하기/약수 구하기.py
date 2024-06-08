N,K = map(int,input().split())

def question(N,K):
    answer_list = []
    for i in range(N):
        if N%(i+1) == 0:
            answer_list.append(i+1)
    answer_list=sorted(answer_list)
    if len(answer_list) < K:
        answer = 0
    else:
        answer = answer_list[K-1]
    return answer

answer = question(N,K)
print(answer)