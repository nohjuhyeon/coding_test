def solution(dartResult):
    number_list = []
    for i in range(len(dartResult)):
        if dartResult[i] == '*':
            number_list[-1] = number_list[-1]*2
            if len(number_list) > 1:
                number_list[-2] = number_list[-2]*2
        elif dartResult[i] == '#':
            number_list[-1] = number_list[-1]*(-1)
        elif dartResult[i] == 'S':
            number_list[-1] = number_list[-1]**1
        elif dartResult[i] == 'D':
            number_list[-1] = number_list[-1]**2
        elif dartResult[i] == 'T':
            number_list[-1] = number_list[-1]**3
        elif dartResult[i]+dartResult[i+1] == '10':
            number_list.append(10)
        elif dartResult[i] == '0' and dartResult[i-1] == '1':
            pass
        else:
            number_list.append(int(dartResult[i]))
    answer = sum(number_list)
    return answer