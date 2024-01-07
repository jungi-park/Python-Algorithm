from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # 큐의 크기 n과 뽑아내려고 하는 수의 개수 m을 입력값으로 받기
position = list(map(int, input().split()))  # 뽑아내려는 수의 위치를 입력값으로 받기
dq = deque([i for i in range(1, n+1)])  # deque([1, 2, 3,...,n])

count = 0   # 2, 3번 수행하면 카운트 올리기

for i in position:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    count+=1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count+=1

print(count)