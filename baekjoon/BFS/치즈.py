n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

d = [(1,0),(-1,0),(0,1),(0,-1)]



from collections import deque

def BFS(sx,sy):
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    queue.append([sx,sy])
    visited[sx][sy] = True
    count = 0
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            nx = x+ dx
            ny = y+ dy
            if(0<=nx<n and 0<=ny<m):
                if(graph[nx][ny]==0 and visited[nx][ny] == False):
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                elif(graph[nx][ny]==1):
                    graph[nx][ny] = 0
                    count +=1
                    visited[nx][ny] = True
    return count

result = []
time = 0
while True:
    time += 1
    count = BFS(0,0)
    result.append(count)
    if count == 0:
        break

print(time-1) # 모든 치즈가 녹는데 걸린 시간
print(result[-2]) # 마지막으로 녹은 치즈의 개수