
import sys
n = int(sys.stdin.readline().rstrip())

def question(n):
    answer_list = []
    for i in range(n):
        k = int(sys.stdin.readline().rstrip())
        if k != 0:
            answer_list.append(k)
        else:
            answer_list.pop()
    answer = sum(answer_list)
    return answer

answer = question(n)
print(answer)