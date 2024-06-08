import sys
from collections import deque

A,B = map(int,sys.stdin.readline().rstrip().split())

def question(A,B):
    answer_list = []
    input_list= deque(range(1,A+1))
    for i in range(A):
        for j in range(B-1):
            input_list.append(input_list[0])
            input_list.popleft()
        answer_list.append(str(input_list[0]))
        input_list.popleft()
    answer = "<{}>".format(", ".join(answer_list))
    return answer

answer = question(A,B)
print(answer)