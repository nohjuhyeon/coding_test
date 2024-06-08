N = int(input())
list_N = set(map(int,input().split()))
M = int(input())
list_M = list(map(int,input().split()))

def question(list_N,list_M,M):
    answer = [0]*M
    for i in range(len(list_M)):
        if list_M[i] in list_N:
            answer[i] = 1
    return answer
answer = question(list_N,list_M,M)
print(*answer)