m,n = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
from collections import deque
def BFS():
    qeueu = deque()
    for i in range(n):
        for j in range(m):
            #익은 토마토를 한번에 큐에 넣고 시작해야함 밖에서 포문으로 BFS()에 하나씩 매개변수로 넣어 주면 안됨
            if graph[i][j] == 1:
                qeueu.append([i, j])
    while qeueu:
        x,y = qeueu.popleft()
        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]
            if  nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif graph[nx][ny] == 0:
                qeueu.append([nx,ny])
                graph[nx][ny] = graph[x][y]+1


BFS()

ans = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            # 안익은 토마토(0)이 있으면 바로 정지
            print(-1)
            exit()
    ans = max(ans, max(line))
# 1에서 시작했기 때문에 결과 값에서 1빼주기
print(ans-1)

