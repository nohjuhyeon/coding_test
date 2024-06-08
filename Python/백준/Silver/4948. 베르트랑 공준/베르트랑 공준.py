import sys
def question():
    while True:
        a = int(sys.stdin.readline().rstrip())
        if a == 0:
            break
        else:
            answer = 0
            answer_list = [1]*(2*a)
            answer_list[0]=0
            repeat = int((2*a)**0.5)+1
            for j in range(2,repeat+1):
                if answer_list[j-1] == 1:
                    for i in range(j*j,2*a+1,j):
                        answer_list[i-1] = 0
            answer = sum(answer_list[a:2*a])
            print(answer)
    return 0
question()
