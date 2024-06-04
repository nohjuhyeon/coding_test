def solution(s):
    first_num = 0
    same_num = 0
    diff_num = 0 
    str_list = []
    for i in range(len(s)):
        first_str = s[first_num]
        if first_str == s[i]:
            same_num += 1
        else:
            diff_num += 1
        if same_num == diff_num:
            str_list.append(s[first_num:i+1])
            first_num = i+1
            same_num = 0
            diff_num = 0
        elif i == len(s) - 1:
            str_list.append(s[i]) 

    answer = len(str_list)
    return answer