import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

def question(N,M):
    list_N = [0]*N
    for i in range(N):
        list_N[i] = sys.stdin.readline().rstrip()
    list_N = set(list_N)
    list_M = []
    for i in range(M):
         answer = sys.stdin.readline().rstrip()
         if answer in list_N:
             list_M.append(answer)
    print(len(list_M))
    list_M.sort(key = lambda x: x)
    for i in range(len(list_M)):
        print(list_M[i])
    return 0

question(N,M)