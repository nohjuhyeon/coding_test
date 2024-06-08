A,B = map(int,input().split())
def question(A,B):
    list_A = list(map(int,input().split()))
    answer_list = []
    for i in range(A):
        for j in range(i+1,A):
            for k in range(j+1,A):
                sum = list_A[i]+list_A[j]+list_A[k]
                if sum <= B:
                    answer_list.append(sum)
    answer = max(answer_list)
    return answer

answer = question(A,B)
print(answer)