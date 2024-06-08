import sys   
N = int(sys.stdin.readline())
def question(N):
    answer_list = list(map(int,sys.stdin.readline().split()))
    answer = list(set(answer_list))
    answer = sorted(answer)
    dic = {}
    for i in range(len(answer)):
        dic[answer[i]] = i
    pass
    answer = [0]*N
    for i in range(len(answer_list)):
        answer[i] = dic[answer_list[i]]
    return answer
answer = question(N)
print(*answer)