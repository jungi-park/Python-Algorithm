import sys
n,m = map(int,sys.stdin.readline().split())

graph =[[]]

for i in range(n):
    graph.append([])

for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]* (n+1)

from collections import deque
def BFS(sx):
    queue = deque([sx])
    while queue:
        x= queue.popleft()
        visited[x] = True
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
    return True

result = 0
for i in range(1,n+1):
    if visited[i] == False:
        BFS(i)
        result+=1

print(result)