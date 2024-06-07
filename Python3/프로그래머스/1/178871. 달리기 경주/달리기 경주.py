def solution(players, callings):
    range_list = list(range(len(players)))
    dict_players = dict(zip(players,range_list))
    dict_numbers = dict(zip(range_list,players))
    for i in callings:
        after_number = dict_players[i]
        before_name = dict_numbers[after_number-1]
        dict_players[i] = after_number-1
        dict_players[before_name] = after_number
        dict_numbers[after_number-1] = i
        dict_numbers[after_number] = before_name
        pass
    dict_players = sorted(dict_players, key=lambda x:dict_players[x])
    return dict_players