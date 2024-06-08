import sys 

N = sys.stdin.readline().rstrip()

def question(N):
    answer = []
    for i in range(len(N)):
        for j in range(len(N)-i):
            answer.append(N[i:j+i+1])
    answer= len(set(answer))
    return answer

answer = question(N)
print(answer)
