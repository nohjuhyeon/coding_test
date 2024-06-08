
N = int(input())

def question(N):
    answer = []
    for i in range(N):
        A,B = input().split()
        answer_element=[int(A),B]
        answer.append(answer_element)
    answer.sort(key=lambda x:(x[0]))
    for i in range(len(answer)):
        print(*answer[i])

question(N)