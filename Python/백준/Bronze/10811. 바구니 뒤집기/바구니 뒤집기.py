N,M = map(int, input().split())
list_output = []
for a in range(N):
    list_output.append(a+1)
for a in range(M):
    i,j = map(int, input().split())
    i = i - 1
    j = j - 1
    repeat = int((j - i)/2) + 1
    for b in range(repeat):
        pass
        list_output[i+b], list_output[j-b] = list_output[j-b],list_output[i+b]
        pass
for c in range(len(list_output)):
    print(list_output[c], end=" ")
pass