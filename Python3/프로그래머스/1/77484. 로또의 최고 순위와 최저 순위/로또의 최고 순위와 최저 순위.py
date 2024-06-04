def solution(lottos, win_nums):
    result = [7,7]
    for i in lottos:
        if i == 0:
            result[0] -= 1
        elif i in win_nums:
            result[0] -= 1
            result[1] -= 1
    if result[0] == 7:
        result[0] = 6
    if result[1] == 7:
        result[1] = 6
    return result