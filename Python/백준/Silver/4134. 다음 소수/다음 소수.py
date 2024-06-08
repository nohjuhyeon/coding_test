import sys

n = int(sys.stdin.readline().rstrip())

def question(n):
    for i in range(n):
        answer_num = int(sys.stdin.readline().rstrip())
        if  answer_num <= 2:
            print(2)
        else:
            answer = 0
            while True:
                repeat = int((answer_num**(0.5)))+2
                for i in range(2,repeat):
                    if answer_num%(i) == 0:
                        answer = 0
                        break
                    else:
                        answer = answer_num
                if answer != 0:
                    break
                else:
                    answer_num += 1
            print(answer)
    return 0

question(n)