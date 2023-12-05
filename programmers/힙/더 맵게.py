import heapq

def solution(scoville, K):
    answer = 0
    heapList = []
    for s in scoville:
        heapq.heappush(heapList, s)
    
    while len(heapList)>=2 and heapList[0] < K:
        one = heapq.heappop(heapList)
        two = heapq.heappop(heapList)
        make = one + two*2
        heapq.heappush(heapList,make)
        answer+=1
    
    if heapList[0] < K:
        answer = -1
        
    
    return answer