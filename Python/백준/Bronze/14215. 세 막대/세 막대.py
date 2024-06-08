list_n = list(map(int,input().split()))

def question(list_n):
    list_n = sorted(list_n)
    if list_n[2] >= list_n[0] + list_n[1]:
        list_n[2] = list_n[0] + list_n[1] -1
    answer = sum(list_n)
    return answer

answer = question(list_n)

print(answer)