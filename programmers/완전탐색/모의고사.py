def solution(answers):
    answer = [0,0,0]
    result = []
    anserArr =[[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i in range(3):
        for d in range(len(answers)):
            if anserArr[i][d%len(anserArr[i])] == answers[d]:
                answer[i] += 1
    maxVal = max(answer)
    
    for i in range(3):
        if answer[i] == maxVal:
            result.append(i+1)
        
    return result