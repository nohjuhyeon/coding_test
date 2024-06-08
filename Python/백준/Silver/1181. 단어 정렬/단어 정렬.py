N = int(input())

def question(N):
    answer = []
    for i in range(N):
        answer.append(input()) 
    answer = list(set(answer))
    answer.sort(key = lambda x:(len(x),x))
    for i in range(len(answer)):
        print(answer[i])
    return answer

answer = question(N)