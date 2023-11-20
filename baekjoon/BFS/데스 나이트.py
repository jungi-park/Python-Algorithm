from collections import deque

n = int(input())

array = list(map(int,input().split()))

visited = [[False]*n for _ in range(n)]



d = [ (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
def BFS():
  queue = deque()
  queue.append([array[0],array[1],0])
  visited[array[0]][array[1]] = True
  while queue:
    x,y,dis = queue.popleft()
    if x == array[2] and y == array[3]:
      return dis
    for dx,dy in d:
      nx = x+dx
      ny = y+dy
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append([nx,ny,dis+1])
  return -1

print(BFS())