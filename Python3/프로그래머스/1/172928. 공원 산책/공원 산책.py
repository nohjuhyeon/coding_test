def solution(park, routes):
    for i in range(len(park)):
        if 'S' in park[i]:
            y = i
            x = park[i].index('S')
    pass
    for i in routes:
        direction = i.split()[0]
        distance = int(i.split()[1])
        check=''
        y_case = y
        x_case = x
        if direction == 'E':
            if len(park[0]) > x+distance:
                for j in range(distance):
                    x_case = x_case+1
                    if park[y_case][x_case] == 'X':
                        check= 'Yes'
        elif direction == 'W':
            if 0 <= x-distance:
                for j in range(distance):
                    x_case = x_case-1
                    if park[y_case][x_case] == 'X':
                        check= 'Yes'
        elif direction == 'N':
            if 0 <= y-distance:
                for j in range(distance):
                    y_case = y_case - 1
                    if park[y_case][x_case] == 'X':
                        check= 'Yes'
        elif direction == 'S':
            if len(park) > y+distance:
                for j in range(distance):
                    y_case = y_case + 1
                    if park[y_case][x_case] == 'X':
                        check= 'Yes'
        if check != 'Yes':
            x = x_case
            y = y_case
    answer = [y,x]
    return answer