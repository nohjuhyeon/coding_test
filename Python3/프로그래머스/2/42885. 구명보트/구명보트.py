from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    answer = 0
    for i in range(len(people)):
        if people[-1] + people[0] <= limit:
          people.pop()
          people.popleft()
          answer += 1
        else:
           people.popleft()
           answer += 1
        if len(people) <= 1:
           break
    answer += len(people)
    return answer