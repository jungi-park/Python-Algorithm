from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

d = [(1,0),(-1,0),(0,1),(0,-1)]
result = 0
picture = 0

def BFS(sx,sy,count):
    qu = deque()
    global result
    qu.append((sx,sy))
    graph[sx][sy] = 0
    while qu :
        x,y = qu.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 :
                    qu.append((nx,ny))
                    count+=1
                    graph[nx][ny] = 0
    result = max(count,result)

for i in range(n):
    for k in range(m):
        if graph[i][k] ==1 :
            BFS(i,k,1)
            picture+=1

print(picture)
print(result)