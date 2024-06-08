N = int(input())

def question(N):
    while True:
        if N == 1:
            break
        else:
            for i in range(2,N+1):
                if N%(i)==0:
                    answer = i
                    break
            N = int(N/answer)
            print(answer)

    return 0

answer = question(N)