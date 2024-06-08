import sys
N = int(sys.stdin.readline().rstrip())

def question(N):
    for i in range(N):
        A,B = map(int,sys.stdin.readline().rstrip().split())
        answer = 0
        for j in range(A):

            if A%(A-j) == 0 and B%(A-j) == 0:
                answer = int((A*B)/(A-j))
                break
        print(answer)

question(N)