def solution(s):
    answer = []
    s = s[2:-2].split("},{")

    s_list = [(i.split(','),len(i.split(','))) for i in s]
    s_list.sort(key=lambda x:x[1])
    for i in s_list:
        for j in i[0]:
            if int(j) not in answer:
                answer.append(int(j))
    return answer