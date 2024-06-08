x,y,w,h = map(int,input().split())

def question(x,y,w,h):
    list_answer = [x,y]
    list_answer.append(w-x)
    list_answer.append(h-y)
    answer= min(list_answer)
    return answer

answer = question(x,y,w,h)
print(answer)