import sys
n = int(sys.stdin.readline().rstrip())

def question(n):
    for i in range(n): 
        answer_list = list(sys.stdin.readline().rstrip())
        answer = 0
        for j in range(len(answer_list)):
            if answer_list[j] == '(':
                answer += 1
            else:
                answer += -1
            if answer < 0:
                break
        if answer == 0:
            print("YES")
        else:
            print("NO")
    return 0

question(n)