N = int(input())
def question(N):
    answer = -1
    if N%5 == 0:
        answer = int(N/5)
    else:
        for i in range(int(N/5)+1):
            M = N - (int(N/5)-i)*5
            if M%3 == 0:
                  answer = int(N/5)-i + int(M/3)
                  break
            else:
               pass

    return answer

answer = question(N)

print(answer)