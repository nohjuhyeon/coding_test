
N,k = map(int,input().split())

def question(N,k):
    answer_list = list(map(int,input().split()))
    answer_list = sorted(answer_list)
    answer = answer_list[N-k]
    return answer

answer = question(N,k)
print(answer)