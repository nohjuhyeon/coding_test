def solution(numbers):
    answer = 0
    for i in range(0,10):
        check = 0
        for j in range(len(numbers)):
            if i == numbers[j]:
                check = check + 1
                pass
        if check == 1:
            pass
        else:
            answer += i
                
    return answer