def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(int(len(score)/m)):
        answer += score[m*i+m-1]*m
    return answer