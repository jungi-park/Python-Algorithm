def solution(brown, yellow):
    answer = []
    allT = brown+yellow
    for b in range(1,allT+1):
        a = (brown - 2*b +4)/2
        if (a-2)*(b-2) == yellow:
            answer.append(a)
            answer.append(b)
            break
    return answer