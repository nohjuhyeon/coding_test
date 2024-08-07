from collections import Counter
def solution(k, tangerine):
    answer = 0
    count_items = Counter(tangerine)
    for i in sorted(count_items.values(),reverse=True):
        k = k - i
        answer += 1
        if k <= 0:
            break
    return answer