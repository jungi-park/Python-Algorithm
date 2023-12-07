def solution(clothes):
    answer = 1
    dic = {}
    for clothe in clothes:
        name , kind = clothe
        if kind in dic:
            dic[kind].append(name)
        else:
            dic[kind] = [name]
      
    for kind in dic:
        # 해당 옷종류를 선택 안하는 경우도 옷으로 생각하면 +1
        answer *= (len(dic[kind])+1)
    # 모든 옷을 선택 안한 경우 즉, 옷을 1가지도 선택하지 않은 경우를 -1
    return answer-1 