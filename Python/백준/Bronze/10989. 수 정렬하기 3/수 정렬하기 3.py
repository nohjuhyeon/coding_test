import sys      

n = int(sys.stdin.readline())

def question(n):
    answer = [0]*10001
    for i in range(n):
        index = int(sys.stdin.readline())
        answer[index] += 1
    for i in range(len(answer)):
        for j in range(answer[i]):
            print(i)
    return 0

question(n)
    