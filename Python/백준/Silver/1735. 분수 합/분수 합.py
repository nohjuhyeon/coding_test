import sys

A,B = map(int,sys.stdin.readline().rstrip().split())
C,D = map(int,sys.stdin.readline().rstrip().split())

def question(A,B,C,D):
    answer_a = A*D+B*C
    answer_b = B*D
    answer = [answer_a,answer_b]
    while answer_b != 0:
        answer_a, answer_b = answer_b, answer_a % answer_b
    repeat = answer_a
    answer = [int(answer[0]/repeat),int(answer[1]/repeat)]
    print(*answer)
    return 0
question(A,B,C,D)
