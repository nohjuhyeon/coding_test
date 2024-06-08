
def question():
    list_A = []
    list_B = []
    answer_A = []
    answer_B=[]
    for i in range(3):
        A,B = map(int,input().split())
        list_A.append(A)
        list_B.append(B)
    set_A = list(set(list_A))
    set_B = list(set(list_B))
    for i in range(len(set_A)):
        if list_B.count(set_B[i]) == 1:
            answer_B = set_B[i]
        if list_A.count(set_A[i]) == 1:
            answer_A = set_A[i]
    answer = [answer_A,answer_B]
    return answer
answer = question()
print(*answer)