def solution(cacheSize, cities):
    cities = [i.lower() for i in cities]
    answer_list = []
    answer = 0
    for i in range(len(cities)):
        if cities[i] in answer_list:
            answer += 1
            answer_list.remove(cities[i])
            answer_list.append(cities[i])
        elif len(answer_list) < cacheSize:
            answer += 5
            answer_list.append(cities[i])
        else:
            answer += 5
            answer_list.append(cities[i])
            answer_list = answer_list[1:]
    return answer