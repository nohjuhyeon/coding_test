N,M = map(int,input().split())

def question(N,M):
    list_N = [0]*N
    list_M = [0]*M
    answer = 0
    for i in range(N):
        list_N[i]=input()
    list_N = set(list_N)
    for i in range(M):
        list_M[i]=input()
    for i in range(M):
        if list_M[i] in list_N:
            answer += 1
    return answer

answer = question(N,M)
print(answer)