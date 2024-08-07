def solution(s):
    answer = 0
    start = '[({'
    for j in range(len(s)):
        answer_list = []
        s_list = s[j:]+s[:j]
        for i in s_list:
            if i in start:
                answer_list.append(i)
            elif len(answer_list) == 0:
                answer_list.append(i)
                break                
            elif i == ']':
                if answer_list[-1] != '[':
                    break
                else:
                    answer_list = answer_list[:-1]
            elif i == '}':
                if answer_list[-1] != '{':
                    break
                else:
                    answer_list = answer_list[:-1]
            elif i == ')':
                if answer_list[-1] != '(':
                    break
                else:
                    answer_list = answer_list[:-1]
        if len(answer_list) == 0:
            answer += 1
    return answer