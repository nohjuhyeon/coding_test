N = int(input())

def question(N):
    answer = {}
    for i in range(N):
        A,B = input().split()
        answer[A] =B
    answer = list(answer.items())
    answer.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(answer)):
        if answer[i][1] == 'enter':
            print(answer[i][0])
    return answer

question(N)