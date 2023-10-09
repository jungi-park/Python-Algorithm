n,m,k = map(int,input().split())

graph = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    r,c = map(int,input().split())
    graph[r][c] = 1

d = [(1,0),(-1,0),(0,-1),(0,1)]

from collections import deque

def BFS(startX,startY):
    queue = deque()
    queue.append([startX,startY])
    graph[startX][startY] = 0
    count = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if nx<=0 or nx>n or ny<=0 or ny>m:
                continue
            if graph[nx][ny] == 1:
                count +=1
                graph[nx][ny] = 0
                queue.append([nx,ny])
    return count
    

result =[]
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j] == 1:
            result.append(BFS(i,j))

print(max(result))