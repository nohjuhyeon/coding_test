def solution(n):
    answers = []
    three = 3
    check = 0
    change = ""
    answer = 0
    while True:
        if n >= three:
            check += 1
            three = three*3
            pass
        else:
            break
    for i in range(check):
        check2 = 0
        while True:
            if n >= 3**(check-i):
                n = n - 3**(check-i)
                check2 += 1
            else:
                break
        answers.append(check2)
    answers.append(n)
    answers.reverse()
    for i in range(len(answers)):
        change = change + str(answers[i])
    change = int(change)
    for i in range(len(str(change))):
        answer = answer + 3**(i)*int(str(change)[-i-1])
        pass
    return answer