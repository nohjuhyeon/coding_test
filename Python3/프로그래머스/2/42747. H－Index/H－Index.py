def solution(citations):
    citations = sorted(citations)
    answer = 0
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            answer = len(citations)-i
            break
    return answer
