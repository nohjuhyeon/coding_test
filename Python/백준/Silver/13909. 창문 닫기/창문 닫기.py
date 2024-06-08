import sys

n = int(sys.stdin.readline().rstrip())

def question(n):
    answer = int(n**0.5)
    return answer
answer = question(n)

print(answer)
