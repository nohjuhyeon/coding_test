def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        str_a = ""
        for j in range(len(p)):
            str_a = str_a + t[i+j]
        num_a = int(str_a)
        if num_a <= int(p):
            answer += 1
    return answer