import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
def question(n):
    input_list = deque(map(int,sys.stdin.readline().rstrip().split()))
    answer_list = deque(range(2,n+1))
    answer = [1]
    for i in range(n-1):
        if input_list[answer[-1]-1] > 0:
            for j in range(input_list[answer[-1]-1]-1):
                answer_list.append(answer_list[0])
                answer_list.popleft()
            answer.append(answer_list[0])
            answer_list.popleft()
        else:
            for j in range(input_list[answer[-1]-1]*-1-1):
                answer_list.appendleft(answer_list[-1])
                answer_list.pop()
            answer.append(answer_list[-1])
            answer_list.pop()
    return answer

answer = question(n)
print(*answer)