def solution(id_list, report, k):
    report = list(set(report))
    report_dict = dict(zip(id_list,[0]*len(id_list)))
    id_dict = {}
    report_list = []
    for i in id_list:
        id_dict[i] = list()
    for i in report:
        id_dict[i.split()[1]].append(i.split()[0])
        if report_dict[i.split()[1]] >= k:
            report_list.append(i.split()[1])
        pass
    for i in id_list:
        if len(id_dict[i]) >= k:
            for j in id_dict[i]:
                report_dict[j] +=1
    answer = list(report_dict.values())
    return answer
