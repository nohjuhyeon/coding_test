def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1_index = 0
    cards2_index = 0
    for i in range(len(goal)):
        if cards1_index < len(cards1) and goal[i] == cards1[cards1_index]:
            cards1_index += 1
        elif cards2_index < len(cards2) and goal[i] == cards2[cards2_index]:
            cards2_index += 1
        else:
            answer = 'No'
            break
    return answer