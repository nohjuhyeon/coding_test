def solution(arr):
    max_num = max(arr)
    n = 1
    while True:
        check=True
        for i in arr:
            if max_num*n%(i) != 0:
                check = False
                break
        if check == True:
            answer = max_num*n
            break
        else:
            n += 1
    return answer