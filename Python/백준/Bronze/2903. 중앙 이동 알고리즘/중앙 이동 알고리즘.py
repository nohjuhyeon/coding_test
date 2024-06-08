N = int(input())

def question(N):
    a = 2
    for i in range(N):
        a= 2*a -1
    answer = a**2
    return answer

answer = question(N)
print(answer)