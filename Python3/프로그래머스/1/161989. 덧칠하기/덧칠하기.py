from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    for i in range(len(section)):
        check_num = section[0]+m-1
        for i in range(len(section)):
            if section[0]<=check_num:
                section.popleft()
            else:
                break
        answer += 1
        if len(section) == 0:
            break
    return answer