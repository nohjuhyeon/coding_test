import sys
n = int(sys.stdin.readline().rstrip())

def question(n):
    input_list = [0]*n
    for i in range(n):
        input_list[i] = int(sys.stdin.readline().rstrip())
        pass
    repeat = max(input_list)
    answer_list = [1]*(repeat+1) 
    answer_list[0] = answer_list[1] = 0   
    for j in range(2,repeat+1):
        for k in range(j*j,repeat+1,j):
            answer_list[k] = 0
    for i in range(n):
        answer = 0
        for j in range(int(input_list[i]/2)+1):
            if answer_list[j] != 0 and answer_list[input_list[i] -j] != 0 :
                answer += 1
        print(answer)
    return 0

question(n)