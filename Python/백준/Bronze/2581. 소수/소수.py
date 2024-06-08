M = int(input())
N = int(input())

def question(M,N):
    list_i = []
    for i in range(M,N+1):
        list_j = []
        for j in range(i):
            if i%(j+1) == 0:
                list_j.append(j)
        if len(list_j) == 2:
            list_i.append(i)
    if len(list_i) == 0:
        print(-1)
    else:
        print(sum(list_i))
        print(min(list_i))
    return 0

answer = question(M,N)