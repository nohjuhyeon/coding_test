import sys 

N = int(sys.stdin.readline().rstrip())
N_dict = list(sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())
M_dict = list(sys.stdin.readline().rstrip().split())
def question(N,M,N_dict,M_dict):
    answer_dict = dict.fromkeys(N_dict,0)
    for i in range(N):
        if N_dict[i] in answer_dict.keys():
            answer_dict[N_dict[i]] += 1
    for i in range(M):
        if M_dict[i] in answer_dict:
            print(answer_dict[M_dict[i]], end=" ")
        else:
            print(0,end=" ")
    return 0

answer = question(N,M,N_dict,M_dict)