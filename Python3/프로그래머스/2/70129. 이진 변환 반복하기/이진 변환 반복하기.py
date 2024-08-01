
def solution(s):
    change_count = 0
    remove = 0
    while s != '1':
        remove += s.count('0')
        s = len(s.replace('0',''))
        answer_s = []
        while True:
            if s == 2:
                answer_s.append('0')
                answer_s.append('1')
                break
            elif s == 1:
                answer_s.append('1')
                break
            else:
                answer_s.append(str(s%2))
                s = s//2
        s = ''.join(list(reversed(answer_s)))
        change_count+=1
    answer = [change_count,remove]
    return answer