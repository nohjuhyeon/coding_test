def solution(s, skip, index):
    list_number = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in skip:
        list_number.remove(i)
    answer = ''
    for i in s:
        answer += list_number[(list_number.index(i)+index)%len(list_number)]
    return answer
