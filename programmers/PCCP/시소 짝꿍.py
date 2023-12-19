# 처음 짠  답 시간초과
def solution(weights):
    answer = 0
    for i,x in enumerate(weights):
        for w in range(i+1,len(weights)):
            if x*2 == weights[w]*2:
                answer+=1
            elif x*2 == weights[w]*3:
                answer+=1
            elif x*2 == weights[w]*4:
                answer+=1
            elif x*3 == weights[w]*2:
                answer+=1
            elif x*3 == weights[w]*3:
                answer+=1
            elif x*3 == weights[w]*4:
                answer+=1
            elif x*4 == weights[w]*2:
                answer+=1
            elif x*4 == weights[w]*3:
                answer+=1
            elif x*4 == weights[w]*4:
                answer+=1  
    return answer

# 인터넷 참고한답
def solution(weights):
    answer = 0
    
    dic = {}
    
    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic:
# 2/2,3/3,4/4 는 값이 같은경우 아래와 같이 같은 수의 조합을 구해서 처리
        if dic[i] > 1:
            answer += (dic[i] * (dic[i]-1)) / 2
# 나머지 경우 3가지
# 2/4 -> 4/2 와 같아서 아래와 같이 처리       
        if i*2 in dic:
            answer += dic[i] * dic[2*i]
# 2/3 == 3/2 와 같아서 아래와 같이 처리  
        if i*2/3 in dic:
            answer += dic[i] * dic[i*2/3]
# 3/4 == 4/3 와 같아서 아래와 같이 처리  
        if i*3/4 in dic:
            answer += dic[i] * dic[i*3/4]

    
    
    
    return answer