import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

def question(n):
    answer_list = deque()
    for i in range(n):
        order = list(sys.stdin.readline().rstrip().split())
        if order[0] == 'push':
            answer_list.append(int(order[1]))
        elif order[0] == 'pop':
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list.popleft())
        elif order[0] == 'size':
            print(len(answer_list))
        elif order[0] == 'empty':
            if len(answer_list) ==0:
                print(1)
            else:
                print(0)    
        elif order[0] == 'front':
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list[0])
        elif order[0] == 'back':
            if len(answer_list) == 0:
                print(-1)
            else:
                print(answer_list[-1])
    return 0

question(n)