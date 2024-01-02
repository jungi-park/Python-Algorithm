def solution(genres, plays):
    answer = []
    dicG = {}
    dicP = {}
    for i in range(len(genres)):
        if genres[i] in dicG :
            dicG[genres[i]] += plays[i]
        else:
            dicG[genres[i]] = plays[i]
    dicG = dict(sorted(dicG.items(), key = lambda x : x[1], reverse = True))
    
    for i in range(len(genres)):
        if genres[i] in dicP :
            dicP[genres[i]].append([i,plays[i]])
        else:
            dicP[genres[i]] = [[i,plays[i]]]
    for i in dicP:
        dicP[i].sort(key = lambda x : (x[1],-x[0]))
        
    for g in dicG:
        twice = 0
        while dicP[g] and twice != 2:
            num ,pCut = dicP[g].pop()
            answer.append(num)
            twice +=1
    
    
    return answer