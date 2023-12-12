from collections import deque
def solution(bandage, health, attacks):
    answer = 0
    time = 0
    dureTime = 0
    maxHealth = health
    attacks = deque(attacks)
    while attacks :
        at,de = attacks[0]
        if time == at:
            at,de = attacks.popleft()
            health -= de
            dureTime = 0
        else:
            t,x,y = bandage
            health += x
            dureTime += 1
        
        if health <= 0 :
            return -1
        
        if dureTime >= t:
            health += y
            dureTime = 0
            
        if health> maxHealth:
            health = maxHealth
            
        time += 1
            
    return health
        