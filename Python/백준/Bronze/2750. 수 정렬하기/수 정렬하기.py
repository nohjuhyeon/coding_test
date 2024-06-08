n = int(input())

def question(n):
    answer= []
    for i in range(n):
        answer.append(int(input()))
    answer = sorted(answer)
    for i in range(len(answer)):
        print(answer[i])
    return 0

question(n)