def solution(n, m):
    answer = []
    list_min_n = []
    list_min_m = []
    list_min = []
    list_max_n = []
    list_max_m=[]
    list_max=[]
    for i in range(n):
        if n%(i+1) == 0:
            list_min_n.append(i+1)
    for i in range(m):
        if m%(i+1) == 0:
            list_min_m.append(i+1)
    for i in range(len(list_min_n)):        
        if list_min_n[i] in list_min_m:
            list_min.append(list_min_n[i])
    answer.append(max(list_min))        
    for i in range(n):
        list_max_m.append(m*(i+1))
    for i in range(m):
        list_max_n.append(n*(i+1))
    for i in range(len(list_max_n)):        
        if list_max_n[i] in list_max_m:
            list_max.append(list_max_n[i])
    answer.append(min(list_max))
    return answer
