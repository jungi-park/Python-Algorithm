import heapq
def solution(operations):
    answer = []
    for st in operations:
        commend, number = st.split()
        if commend =="I":
            heapq.heappush(answer,int(number))
        else:
            if number == "1" and answer:
                answer = answer[:-1]
            elif answer:
                heapq.heappop(answer)
    if answer:
        answer = [max(answer), min(answer)]
    else:
        answer= [0, 0]
    return answer