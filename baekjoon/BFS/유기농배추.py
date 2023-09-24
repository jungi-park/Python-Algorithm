t = int(input())
answer = []

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque

def BFS(graph,startX,startY):
    queue = deque([[startX,startY]])
    graph[startX][startY] = 0
    result = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                result +=1
                queue.append([nx,ny])
    return result


for k in range(t):
    result = []
    graph = []
    m,n,k = map(int,input().split())
    for i in range(n):
        graph.append([0]*m)
    for i in range(k):
        y,x = map(int,input().split())
        graph[x][y] = 1
    for i in range(n):
        for k in range(m):
            if graph[i][k] == 1:
                result.append(BFS(graph,i,k))
    answer.append(len(result)) 

for i in answer:
    print(i)