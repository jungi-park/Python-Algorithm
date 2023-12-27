from collections import deque

def solution(queue1, queue2):
    count = 0
    answer = -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while queue1 and queue2 and count != len(queue1)*2:
        if sum1 == sum2:
            answer = count
            break
        elif sum1 > sum2:
            num = queue1.popleft()
            sum1 -= num
            sum2 += num
            queue2.append(num)
        else:
            num = queue2.popleft()
            sum2 -= num
            sum1 += num
            queue1.append(num)
        
        count += 1
    
    return answer
