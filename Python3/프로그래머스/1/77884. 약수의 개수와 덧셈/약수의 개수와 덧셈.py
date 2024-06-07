def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        list_i = []
        for j in range(i+1):
            if i%(j+1) == 0:
                list_i.append(j+1)
        if len(list_i)%2 == 0:
            answer += i
        else:
            answer -= i
    return answer