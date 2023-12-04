from collections import deque
def solution(s):
    answer = True
    s = deque(s)
    left = 0
    
    while s :
        x = s.popleft()
        if x =="(":
            left +=1
        if x ==")":
            left -=1
        if left < 0:
            answer = False
            break
    if left > 0:
        answer = False
    
    return answer