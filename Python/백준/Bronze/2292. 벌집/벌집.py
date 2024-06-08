N = int(input())

def question(N):
    a = 0
    b= 0 
    while True:
        if N - (a)*6 - 1 <= 0:
            b += 1
            break
        else:
            b+=1
        a += b
    answer = b
    return answer


answer = question(N)
print(answer)

