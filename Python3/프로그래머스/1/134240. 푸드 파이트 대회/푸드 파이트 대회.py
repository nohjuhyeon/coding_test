def solution(food):
    answer = ''
    repeat = []
    for i in range(1,len(food)):
        repeat.append(int(food[i]/2))
    print(repeat)
    for i in range(len(repeat)):
        for j in range(repeat[i]):
            answer += str(i+1)
    answer += '0'    
    repeat = list(reversed(repeat))
    for i in range(len(repeat)):
        for j in range(repeat[i]):
            answer += str(len(repeat)-i)
    return answer
