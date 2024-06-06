def solution(board, h, w):
    if len(board) == 1:
        answer = 0
    else:
        if h == 0:
            if w == 0:
                board_list = [board[h+1][w],board[h][w+1]]
            elif w == len(board[0])-1:
                board_list = [board[h+1][w],board[h][w-1]]
            else:
                board_list = [board[h+1][w],board[h][w+1],board[h][w-1]]
        elif h == len(board)-1:
            if w == 0:
                board_list = [board[h-1][w],board[h][w+1]]
            elif w == len(board[0])-1:
                board_list = [board[h-1][w],board[h][w-1]]
            else:
                board_list = [board[h-1][w],board[h][w+1],board[h][w-1]]
        else:
            if w == 0:
                board_list = [board[h-1][w],board[h+1][w],board[h][w+1]]
            elif w == len(board[0])-1:
                board_list = [board[h-1][w],board[h+1][w],board[h][w-1]]
            else:
                board_list = [board[h-1][w],board[h+1][w],board[h][w+1],board[h][w-1]]
        answer = board_list.count(board[h][w])
    return answer