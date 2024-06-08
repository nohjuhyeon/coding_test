import sys      

n = int(sys.stdin.readline())

def question(n):
    answer = [0]*n
    for i in range(n):
        answer[i]= int(sys.stdin.readline())
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
    return 0

question(n)
    