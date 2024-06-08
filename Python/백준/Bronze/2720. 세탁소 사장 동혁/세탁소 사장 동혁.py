T = int(input())

def question(T):
    for i in range(T):
        C = int(input())
        answer = []
        answer.append(int(C/25))
        C = int(C%25)
        answer.append(int(C/10))
        C = int(C%10)
        answer.append(int(C/5))
        answer.append(int(C%5))
        print(*answer)
    return 0

answer = question(T)