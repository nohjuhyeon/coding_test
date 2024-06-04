def solution(babbling):
    list_babbling = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        str_answer = ''
        last_babbling = ''
        while True:
            babbling_str = babbling[i]
            for j in range(len(list_babbling)):
                if babbling[i].startswith(list_babbling[j]) and last_babbling != list_babbling[j]:
                    babbling[i] = babbling[i][len(list_babbling[j]):]
                    str_answer = str_answer+list_babbling[j]
                    last_babbling = list_babbling[j]
                    break
            if babbling_str == babbling[i]:
                break
            else:
                babbling_str = babbling[i]
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace(" ","")
    answer = babbling.count("")
    return answer