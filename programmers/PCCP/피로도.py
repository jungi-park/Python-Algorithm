def solution(k, dungeons):
    answerOne = 0
    answerTwo = 0
    kOne = k
    kTwo = k
    dungeons.sort(key = lambda x : (-(x[0]-x[1]),x[1]))
    for need,damege in dungeons:
        if kOne>=need:
            answerOne +=1
            kOne -=damege
    dungeons.sort(key = lambda x : x[1])
    for need,damege in dungeons:
        if kTwo>=need:
            answerTwo +=1
            kTwo -=damege
    
    answer = max(answerTwo,answerOne)
    return answer