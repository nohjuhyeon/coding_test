
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

def question(n):
    answer_list = deque()
    for i in range(n):
        input_list = list(map(int,sys.stdin.readline().rstrip().split()))
        if input_list[0] == 1:
            answer_list.appendleft(input_list[1])
        elif input_list[0] == 2:
            answer_list.append(input_list[1])
        elif input_list[0] == 3:
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list[0])
                answer_list.popleft()
        elif input_list[0] == 4:
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list[-1])
                answer_list.pop()
        elif input_list[0] == 5:
            print(len(answer_list))
        elif input_list[0] == 6:
            if len(answer_list) == 0:
                print(1)
            else:
                print(0)
        elif input_list[0] == 7:
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list[0])
        elif input_list[0] == 8:
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list[-1])
    return 0

question(n)