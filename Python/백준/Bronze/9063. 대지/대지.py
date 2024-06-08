N = int(input())
def question(N):
    list_A = []
    list_B = []
    for i in range(N):
        A,B = map(int,input().split())
        list_A.append(A)
        list_B.append(B)
    answer = (max(list_A)-min(list_A))*(max(list_B)-min(list_B))
    return answer

answer = question(N)
print(answer)