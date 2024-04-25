def solution(n):
    repeat = int(n**0.5)+1
    answer_list = set()
    for i in range(2,repeat+1):
        for j in range(i*i,n+1,i):
            answer_list.add(j)
    answer = n - 1 - len(answer_list)
    return answer