def solution(answers):
    student_a = [1,2,3,4,5]
    student_b = [2,1,2,3,2,4,2,5]
    student_c = [3,3,1,1,2,2,4,4,5,5]
    answer_a = 0
    answer_b = 0
    answer_c = 0
    for i in range(len(answers)):
        if student_a[int(i%len(student_a))] == answers[i]:
            answer_a += 1
        if student_b[int(i%len(student_b))] == answers[i]:
            answer_b += 1
        if student_c[int(i%len(student_c))] == answers[i]:
            answer_c += 1
    answer = []
    if answer_a == max(answer_a,answer_b,answer_c):
        answer.append(1)
    if answer_b == max(answer_a,answer_b,answer_c):
        answer.append(2)
    if answer_c == max(answer_a,answer_b,answer_c):
        answer.append(3)
    return answer