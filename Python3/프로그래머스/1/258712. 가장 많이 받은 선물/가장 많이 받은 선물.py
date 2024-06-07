
def solution(friends, gifts):
    friends_id = dict(zip(friends,range(len(friends))))
    friend_give = {}
    friend_achieve = {}
    friend_total = {}
    for i in friends:
        friend_give[i] = [0]*len(friends)
        friend_achieve[i] = [0]*len(friends)
        friend_total[i] = [0]*len(friends)
    for i in gifts:
        friend_give[i.split()[0]][friends_id[i.split()[1]]] += 1
        friend_achieve[i.split()[1]][friends_id[i.split()[0]]] += 1
    answer_list = []
    for i in friends:
        for j in range(len(friend_total[i])):
            if friend_give[i][j] - friend_achieve[i][j] > 0:
                friend_total[i][j] += 1
            elif friend_give[i][j] - friend_achieve[i][j] == 0:
                if (sum(friend_give[i])-sum(friend_achieve[i])) > (sum(friend_give[friends[j]])-sum(friend_achieve[friends[j]])):
                    friend_total[i][j] += 1
        answer_list.append(sum(friend_total[i]))
    answer = max(answer_list)
    return answer