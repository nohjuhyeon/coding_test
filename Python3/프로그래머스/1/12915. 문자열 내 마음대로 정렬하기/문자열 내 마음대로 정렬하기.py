def solution(strings, n):
    list_number = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]   
    list_num = []
    list_check = []
    answer = []
    for i in range(len(strings)):
        str_index = ""
        for j in range(len(strings[i])):
            if list_number.index(strings[i][j]) < 10 : 
                str_index += "0"
            str_index += str(list_number.index(strings[i][j]))
        list_num.append(str_index)
    for i in range(len(list_num)):
        if int(list_num[i][2*n]+list_num[i][2*n+1]) not in list_check:
            list_check.append(int(list_num[i][2*n]+list_num[i][2*n+1]))
    list_check = sorted(list_check)
    for i in range(len(list_check)):
        list_index_check = []
        for j in range(len(list_num)):
            if int(list_num[j][2*n]+list_num[j][2*n+1]) == list_check[i]:
                list_index_check.append(list_num[j])
        list_index_check = sorted(list_index_check)
        for j in range(len(list_index_check)):
            answer.append(strings[list_num.index(list_index_check[j])])
    return answer