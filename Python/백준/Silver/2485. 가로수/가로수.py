import sys
n = int(sys.stdin.readline().rstrip())

def question(n):
    answer_first =  int(sys.stdin.readline().rstrip())
    answer_second = int(sys.stdin.readline().rstrip())
    answer_a = answer_second-answer_first
    answer_first = answer_second
    answer_sum = answer_a
    for i in range(n-2):
        answer_second = int(sys.stdin.readline().rstrip())
        answer_b = answer_second-answer_first
        answer_first = answer_second
        answer_sum += answer_b
        while answer_b != 0:
            answer_a, answer_b = answer_b, answer_a % answer_b
    answer = int(answer_sum/answer_a)-n+1
    return answer
answer = question(n)
print(answer)
