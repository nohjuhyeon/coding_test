import sys
def question():
        A,B = map(int,sys.stdin.readline().rstrip().split())
        answer = 0
        for j in range(A):
            if A%(A-j) == 0 and B%(A-j) == 0:
                print(int((A*B)/(A-j)))
                break

question()