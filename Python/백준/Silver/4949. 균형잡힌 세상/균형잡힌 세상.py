import sys

def question():
    while True:
        input_list = sys.stdin.readline().rstrip()
        if input_list == '.':
            break
        else:
            input_list = list(input_list)
            open_list = ['(','[']
            close_list = [')',']']
            answer_list = []
            for i in range(len(input_list)):
                if input_list[i] in open_list:
                    answer_list.append(input_list[i])
                elif input_list[i] == close_list[0]:
                    if len(answer_list) == 0:
                        answer_list.append(input_list[i])
                        break
                    elif answer_list[-1] == '(':
                        answer_list.pop()
                    else:
                        answer_list.append(input_list[i])
                        break
                elif input_list[i] == close_list[1]:
                    if len(answer_list) == 0:
                        answer_list.append(input_list[i])
                        break
                    elif answer_list[-1] == '[':
                        answer_list.pop()
                    else:
                        answer_list.append(input_list[i])
                        break
                else:
                    pass
            if len(answer_list) == 0:
                print('yes')
            else:
                print('no')
    return 0

question()
