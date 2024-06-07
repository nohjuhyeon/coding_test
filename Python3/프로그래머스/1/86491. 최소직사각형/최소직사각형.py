def solution(sizes):
    list_sizes = []
    for i in range(len(sizes)):
        list_sizes.append([max(sizes[i]),min(sizes[i])])
    x = list_sizes[0][0]
    y = list_sizes[0][1]
    for i in range(1,len(list_sizes)):
        if list_sizes[i][0] > x:
            x = list_sizes[i][0] 
        if list_sizes[i][1] > y:
            y = list_sizes[i][1] 
    answer = x*y
    return answer