def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    reserve_list = []
    lost_list = []
    for i in lost:
        if i not in reserve:
            lost_list.append(i)
    for i in reserve:
        if i not in lost:
            reserve_list.append(i)
    
    for i in reserve_list:
        if i-1 in lost_list:
            lost_list.remove(i-1)
        elif i+1 in lost_list:
            lost_list.remove(i+1)
    answer = n - len(lost_list)
    return answer