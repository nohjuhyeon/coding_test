import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

def question(n):
    answer_list = deque(range(1,n+1))
    for i in range(n-1):
        answer_list.popleft()
        answer_list.append(answer_list[0])
        answer_list.popleft()

    return answer_list[0]

answer = question(n)

print(answer)