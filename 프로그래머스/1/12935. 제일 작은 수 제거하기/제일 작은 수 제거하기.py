def solution(arr):
    num_min = min(arr)
    arr.remove(num_min)
    if len(arr) == 0:
        answer = [-1]
    else:  
        answer = arr
    return answer