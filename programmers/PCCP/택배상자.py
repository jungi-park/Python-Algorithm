from collections import deque

def solution(order):
    answer = 0
    Belt = deque(range(1, len(order) + 1))
    bojoBelt = deque()
    order = deque(order)
    
    while order:
        x = order.popleft()
        
        if bojoBelt and bojoBelt[-1] == x:
            bojoBelt.pop()
            answer += 1
        elif Belt and Belt[0] == x:
            Belt.popleft()
            answer += 1
        else:
            if x in Belt:
                finded = Belt.index(x)
                for i in range(finded):
                    bojoBelt.append(Belt.popleft())
                Belt.popleft()
                answer += 1
            else:
                break
    
    return answer
