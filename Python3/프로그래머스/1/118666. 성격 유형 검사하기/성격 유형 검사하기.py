def solution(survey, choices):
    dict_survey = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] > 4:
            dict_survey[survey[i][1]] += choices[i] -4
        elif choices[i] < 4:
            dict_survey[survey[i][0]] += 4 - choices[i] 
    answer = ''
    if dict_survey['T'] > dict_survey['R']:
        answer += 'T'
    else:
        answer += 'R'
    if dict_survey['F'] > dict_survey['C']:
        answer += 'F'
    else:
        answer += 'C'
    if dict_survey['M'] > dict_survey['J']:
        answer += 'M'
    else:
        answer += 'J'
    if dict_survey['N'] > dict_survey['A']:
        answer += 'N'
    else:
        answer += 'A'
    return answer