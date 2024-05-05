N, M = map(int, input().split())
list_N = []
for a in range(N):
    list_N.append(a+1)
pass
for b in range(M):
    i, j = map(int, input().split())
    list_N[i-1],list_N[j-1]=list_N[j-1],list_N[i-1]
    pass
for c in range(len(list_N)):
    print(list_N[c], end = " ")
    pass
