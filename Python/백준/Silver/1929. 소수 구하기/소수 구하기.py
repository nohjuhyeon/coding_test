import sys
A,B = map(int,sys.stdin.readline().rstrip().split())

def question(A,B):
    for i in range(A,B+1):
        if i <= 1:
            pass
        elif i == 2:
            print(2)
        else:
            repeat = int(i**(0.5))+1
            answer= 0
            for j in range(2,repeat+1):
                if i%j == 0:
                    answer = 0
                    break
                else:
                    answer = i
            if answer != 0:
                print(answer)
    return 0

question(A,B)