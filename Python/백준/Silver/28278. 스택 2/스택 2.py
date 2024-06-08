
import sys

n = int(sys.stdin.readline().rstrip())

def question(n):
    answer_list = []
    for i in range(n):
        X = list(map(int,sys.stdin.readline().rstrip().split()))
        if X[0] == 2:
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list[-1])
                answer_list.pop()
        elif X[0]== 3:
            print(len(answer_list))
        elif X[0]== 4:
            if len(answer_list) == 0:
                print(1)
            else:
                print(0)
        elif X[0]== 5:
            if len(answer_list)== 0:
                print(-1)
            else:
                print(answer_list[-1])
        else:
                answer_list.append(X[1])
    return 0
question(n)