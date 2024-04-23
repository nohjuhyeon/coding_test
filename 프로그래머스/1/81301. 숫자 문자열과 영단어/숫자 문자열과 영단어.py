def solution(s):
    list_str = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(len(list_str)):
        if list_str[i] in s:
            s = s.replace(list_str[i],str(i))
    answer = int(s)
    return answer