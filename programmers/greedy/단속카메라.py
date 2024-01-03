def solution(routes):
    routes.sort(key = lambda x : (x[0],x[1]))
    distans = 30001
    answer = 0
    while routes:
        end,start = routes.pop()
        if end<=distans<=start:
            continue
        elif distans > end:
            distans = end
            answer+=1
    return answer