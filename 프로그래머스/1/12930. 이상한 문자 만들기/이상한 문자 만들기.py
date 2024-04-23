def solution(s):
    list_s = list(s)
    num_check = 0
    answer = ""
    for i in range(len(list_s)):
        if list_s[i] ==" ":
            str_answer = " "
            num_check = 0
        else: 
            if num_check% 2 == 0:
                str_answer = list_s[i].upper()
                num_check += 1
            else:
                str_answer = list_s[i].lower()
                num_check += 1
        pass
        answer = answer + str_answer
    return answer