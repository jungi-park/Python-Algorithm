# 문제풀이 실패...

from collections import deque
n,m = map(int,input().split())

graphA = [list(map(str,input())) for _ in range(n) ]
graphB = [list(map(str,input())) for _ in range(n) ]

visited = [ [False]*m for _ in range(n)]


d = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS(sx,sy):
  ori = graphA[sx][sy]
  want = graphB[sx][sy]
  queue = deque()
  queue.append([sx,sy])
  visited[sx][sy] = True
  while queue:
    x,y = queue.popleft()
    for dx,dy in d:
      nx = x+dx
      ny = y+dy
      if 0<= nx < n and 0<= ny < m and not visited[nx][ny] and graphA[nx][ny]==ori:
        visited[nx][ny] = True
        graphA[sx][sy] = want
        graphA[nx][ny] = want
        queue.append([nx,ny])

for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      BFS(i,j)

result = "YES"
for i in range(n):
  for j in range(m):
    if graphA[i][j] != graphB[i][j]:
      result = "NO"
      break
      
print(result)