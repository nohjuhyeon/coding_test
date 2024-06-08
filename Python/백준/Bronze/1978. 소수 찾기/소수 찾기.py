N = int(input())
M = list(map(int,input().split()))
def question(N,M):
    answer = 0
    for i in range(N):
        list_M = []
        for j in range(M[i]):
            if M[i]%(j+1) == 0:
                list_M.append(j+1)
        if len(list_M) == 2:
            answer += 1
    return answer

answer = question(N,M)
print(answer)