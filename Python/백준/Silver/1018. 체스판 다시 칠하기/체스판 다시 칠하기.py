N,M = map(int,input().split())

def question(N,M):
    list_chess = []
    answer = 0
    list_chess_answer = ["WBWBWBWB","BWBWBWBW"]
    for i in range(N):
        list_chess.append(input())
    repeat_x = M-7
    repeat_y = N-7
    answer_list = []
    for i in range(repeat_y):
        for j in range(repeat_x):
            answer_check_start = 0
            answer_check_end = 0
            for k in range(8):
                for l in range(8):
                    if (k)%2 == 1:
                        if list_chess_answer[0][l] != list_chess[i+k][j+l]:
                            answer_check_start += 1
                        if list_chess_answer[1][l] != list_chess[i+k][j+l]:
                            answer_check_end += 1
                    elif (k)%2 == 0:
                        if list_chess_answer[1][l] != list_chess[i+k][j+l]:
                            answer_check_start += 1
                        if list_chess_answer[0][l] != list_chess[i+k][j+l]:
                            answer_check_end += 1
            answer_check = min(answer_check_start,answer_check_end)
            answer_list.append(answer_check)
    answer = min(answer_list)
    return answer 

answer = question(N,M)
print(answer)