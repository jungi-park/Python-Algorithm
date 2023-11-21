from collections import deque


def BFS(s,e):
  queue = deque()
  queue.append([s,e,0])
  while queue:
    a,b,c =queue.popleft()
    if a==b:
      return c
    for i in range(2):
        if i == 0  and a*2 <= b+3:
          queue.append([a*2,b+3,c+1])
        elif i == 1  and a+1 <= b:
          queue.append([a+1,b,c+1])

for _ in range(int(input())):
    s, t = map(int, input().split())
    print(BFS(s, t))
