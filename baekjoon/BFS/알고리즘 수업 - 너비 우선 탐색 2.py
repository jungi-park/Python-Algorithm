from collections import deque
import sys

n,m,r = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  x,y = map(int,sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [ 0 for _ in range(n+1)]

def BFS(graph,r,visited,n):
  queue = deque()
  result = [0]*(n+1)
  count = 1
  queue.append(r)
  visited[r] = 1
  result[r] = count
  while queue:
    x = queue.popleft()
    for i in sorted(graph[x],reverse=True):
      if visited[i] == 0:
        visited[i] = 1
        count += 1
        result[i] = count
        queue.append(i)
  return result

print(*BFS(graph,r,visited,n)[1:])