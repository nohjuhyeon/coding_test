def solution(bandage, health, attacks):
    attack_time = []
    attack_dmg = []
    max_health = health
    cool_time = 0
    for i in attacks:
        attack_time.append(str(i[0]))
        attack_dmg.append(i[1])
    for i in range(int(attack_time[-1])+1):
        if str(i) in attack_time:
            health = health - attack_dmg[attack_time.index(str(i))]
            cool_time = 0
        elif health > 0:
            cool_time += 1
            health += bandage[1]
            if cool_time == bandage[0]:
                health += bandage[2]
                cool_time = 0
            if health > max_health:
                health = max_health
    if health <= 0:
        answer = -1
    else:
        answer = health
    return answer