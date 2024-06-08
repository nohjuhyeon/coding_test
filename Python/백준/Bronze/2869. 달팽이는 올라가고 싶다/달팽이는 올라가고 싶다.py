A,B,V = map(int,input().split())
def question(A,B,V):
    answer = int((V-A)/(A-B))+1
    if int((V-A)%(A-B))!=0:
        answer +=1
    return answer

answer = question(A,B,V)
print(answer)
