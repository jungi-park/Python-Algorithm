from collections import deque

n,m = map(int,input().split())
jnX,jnY,findX,findY = map(int,input().split())
graph = [ list(map(str,input())) for _ in range(n) ]
d = [(0,1),(0,-1),(1,0),(-1,0)]
visited = set()

def BFS():
    queue = deque()
    queue.append((jnX-1,jnY-1,1))
    visited.add((jnX-1,jnY-1))
    while queue :
        x,y,jump = queue.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if nx == findX-1 and ny == findY-1:
                return jump
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited:
                if graph[nx][ny] == "1":
                    queue.append((nx,ny,jump+1))
                    visited.add((nx,ny))
                    graph[nx][ny]=0
                else:
                    queue.appendleft((nx,ny,jump))
                    visited.add((nx,ny))
                    graph[nx][ny]=0
        
print(BFS())