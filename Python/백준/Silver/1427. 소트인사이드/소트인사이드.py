N = list(input())

def question(N):
    for i in range(len(N)):
        N[i] = int(N[i])
    N.sort()
    N.reverse()
    for i in range(len(N)):
        N[i] = str(N[i])
    answer = ''.join(N)
    return answer

answer = question(N)
print(answer)