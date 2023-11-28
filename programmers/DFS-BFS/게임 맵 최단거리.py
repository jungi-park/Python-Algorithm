from collections import deque

d = [(1,0),(-1,0),(0,1),(0,-1)]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = BFS(0,0,0,maps,n,m)
    return answer

def BFS(sx,sy,count,maps,n,m):
    queue = deque()
    queue.append([sx,sy,count])
    maps[sx][sy] = 0
    while queue:
        x,y,c = queue.popleft()
        if x == n-1 and y == m-1:
            return c+1
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append([nx,ny,c+1])
    return -1