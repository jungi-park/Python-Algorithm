from collections import deque 
n,m,k = map(int,input().split())

graph =[[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    x,y = map(int,input().split())
    graph[x][y] = 1

d =[(1,1),(1,-1),(-1,1),(-1,-1)]


def bfs(sx,sy):
    visited = [[False]*(m+1) for _ in range(n+1)]
    queue = deque()
    queue.append([sx,sy])
    graph[sx][sy] = 0
    visited[sx][sy] = True
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            nx = x+ dx
            ny = y+ dy
            if 0<nx<=n and 0<ny<=m and not graph[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = 1
                queue.append([nx,ny])


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i,j)

result = "YES"
for array in graph:
    if 0 in array:
        result = "NO"
        break

print(result)