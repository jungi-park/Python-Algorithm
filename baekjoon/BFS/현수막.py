n,m = map(int,input().split())


graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))


d = [(1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]

from collections import deque

def BFS(sx,sy):
    queue = deque()
    queue.append([sx,sy])
    graph[sx][sy] = 0

    while queue:
        x,y = queue.popleft()

        for dx,dy in d:
            nx = x+ dx
            ny = y+ dy

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] != 0:
                graph[nx][ny] = 0
                queue.append([nx,ny])

count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            count +=1
            BFS(i,j)

print(count)