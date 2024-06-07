def solution(today, terms, privacies):
    terms_dict = {}
    answer = []
    today = int(''.join(today.split('.')))

    for i in terms:
        terms_dict[i.split()[0]] = int(i.split()[1])*28
    for i in range(len(privacies)):
        date = privacies[i].split()[0]
        limit_date = terms_dict[privacies[i].split()[1]]-1
        date = [int(date.split('.')[0]),int(date.split('.')[1]),int(date.split('.')[2])]
        date[2] += limit_date
        while True:
            if date[2] > 28:
                date[2] = date[2] - 28
                date[1] += 1
            else:
                break
        while True:
            if date[1] > 12:
                date[1] = date[1] - 12
                date[0] += 1
            else:
                break
        date = [str(date[0]),str(date[1]),str(date[2])]
        if len(date[1]) == 1:
            date[1] = '0' + date[1]
        if len(date[2]) == 1:
            date[2] = '0' + date[2]
        date = int(''.join(date))
        if date < today:
            answer.append(i+1)
    return answer
