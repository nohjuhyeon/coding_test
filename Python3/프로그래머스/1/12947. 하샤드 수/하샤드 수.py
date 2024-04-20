def solution(x):
    sum_x = 0
    y = str(x)
    for i in range(len(y)):
        sum_x += int(y[i])
    answer = x%sum_x == 0
    return answer