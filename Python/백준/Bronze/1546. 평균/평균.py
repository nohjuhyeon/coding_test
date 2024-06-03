N = int(input())
list_score = list(map(int, input().split()))
list_score_list = []
sum = 0
for i in range(N):
    list_score_list.append(list_score[i])
    pass
max = max(list_score_list)
for i in range(N):
    list_score_list[i]=((list_score_list[i]/max)*100)
    sum = sum + list_score_list[i]
print(sum/N)