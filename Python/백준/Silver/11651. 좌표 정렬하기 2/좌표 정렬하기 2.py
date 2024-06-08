N = int(input())

def question(N):
    answer = []
    for i in range(N):
        A,B = map(int,input().split())
        answer.append((A,B)) 
    answer.sort(key = lambda x:(x[1],x[0]))
    for i in range(len(answer)):
        print(answer[i][0],answer[i][1])
    return answer

answer = question(N)
