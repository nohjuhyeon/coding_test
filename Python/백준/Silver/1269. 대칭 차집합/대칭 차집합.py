import sys
N,M = map(int,sys.stdin.readline().rstrip().split())

def question(N,M):
    answer = 0
    list_N = list(map(int,sys.stdin.readline().rstrip().split()))
    list_N.extend(list(map(int,sys.stdin.readline().rstrip().split())))
    list_N = set(list_N)
    answer = len(set(list_N))*2 - M -N
    return answer 

answer = question(N,M)
print(answer)