import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
A = deque(map(int,sys.stdin.readline().rstrip().split()))
B = deque(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
C = deque(map(int,sys.stdin.readline().rstrip().split()))

def question(N,A,B,M,C):
    answer_list = deque()
    for i in range(N):
        if A[i] == 0:
            answer_list.append(B[i])
    for i in range(M):
        answer_list.appendleft(C[0])
        C.append(answer_list[-1])
        answer_list.pop()
        C.popleft()
    answer = C
    return answer

answer = question(N,A,B,M,C)

print(*answer)
