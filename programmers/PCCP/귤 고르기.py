def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    dic ={}
    for i in tangerine:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    for key in dic:
        answer+=1
        k -= dic[key]
        if k <=0:
            break
    return answer
