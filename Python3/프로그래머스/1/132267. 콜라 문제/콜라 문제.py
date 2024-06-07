def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += int((n/a))*b
        n = n - int(n/a)*a + int((n/a))*b
    return answer