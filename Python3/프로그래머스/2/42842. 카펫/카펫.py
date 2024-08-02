def solution(brown, yellow):
    for i in range(brown+yellow):
        if (brown+yellow)%(i+1)==0 and brown ==(i-1)*2 + ((brown+yellow)//(i+1))*2 and yellow == (i-1)*((brown+yellow)//(i+1)-2):
            answer = [(brown+yellow)//(i+1),i+1]
            break
    return answer
