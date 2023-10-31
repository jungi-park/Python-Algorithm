n = int(input())

graph = [list(map(int,input()))for _ in range(n)]

d =[(1,0),(-1,0),(0,-1),(0,1)]

visited =[[-1]*n for _ in range(n)]


from collections import deque

def BFS():
    queue = deque()
    queue.append([0,0,0])
    visited[0][0] = 0
    while queue:
        x,y,z = queue.popleft()
        if x == n-1 and y == n-1:
            return
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                if graph[nx][ny] == 0: 
                    visited[nx][ny] = z+1
                    queue.append([nx,ny,z+1])
                else:
                    visited[nx][ny] = z
                    queue.appendleft([nx,ny,z])

BFS()
print(visited[n - 1][n - 1])