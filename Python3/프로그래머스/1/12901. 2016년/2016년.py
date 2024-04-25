def solution(a, b):
    dict_month = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    days_of_name = ['FRI','SAT','SUN','MON','TUE','WED','THU',]
    answer_num = b
    for i in range(a-1):
        answer_num += dict_month[i+1]
    answer_num = int(answer_num%7)
    answer = days_of_name[answer_num-1]
    return answer
