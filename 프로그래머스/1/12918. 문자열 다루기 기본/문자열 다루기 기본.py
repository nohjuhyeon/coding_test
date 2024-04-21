def solution(s):
    try:
        int(s)
        answer = (len(s) == 4 or len(s) == 6)

    except:
        answer = False
    return answer