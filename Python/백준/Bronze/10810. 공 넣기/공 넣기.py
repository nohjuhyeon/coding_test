
N, M = map(int, input().split())
list_N = []
for a in range(N):
    list_N.append(0)
pass
for b in range(M):
    i, j, k = map(int, input().split())
    for c in range(i-1,j):
        list_N[c] = k
        pass
    pass
for c in range(len(list_N)):
    print(list_N[c], end = " ")
    pass
