def solution(arr):
    num_arr = arr[0]
    answer = [arr[0]]
    for i in range(len(arr)):
        if num_arr != arr[i]:
            num_arr = arr[i]
            answer.append(num_arr)
    return answer