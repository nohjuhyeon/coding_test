import sys 

N,M = map(int,sys.stdin.readline().split())

def question(N,M):
    answer = {}
    for i in range(N):
        answer[sys.stdin.readline().strip('\n')]=str(i+1)
    convert_answer = {v:k for k,v in answer.items()}
    for i in range(M):
        quest = sys.stdin.readline().strip('\n')
        if quest in answer.keys():
            print(answer[quest])
        else:
            print(convert_answer[quest])
question(N,M)

