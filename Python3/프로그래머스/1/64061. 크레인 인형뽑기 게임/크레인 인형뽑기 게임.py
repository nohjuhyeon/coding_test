def solution(board, moves):
    board_list = []
    answer_list = []
    answer = 0
    for i in range(len(board)):
        board_list.append([])
    for i in board:
        for j in range(len(i)):
            if i[j] != 0:
                board_list[j].append(i[j])
    for i in moves:
        if len(answer_list) != 0 and len(board_list[i-1]) != 0 and board_list[i-1][0] == answer_list[-1]:
            answer_list = answer_list[:-1]
            board_list[i-1] = board_list[i-1][1:]
            answer += 2
        else:
            if len(board_list[i-1]) != 0 and board_list[i-1][-1] != 0:
                answer_list.append(board_list[i-1][0])
                board_list[i-1] = board_list[i-1][1:]
    return answer