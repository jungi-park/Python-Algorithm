from itertools import combinations
from copy import deepcopy
from collections import deque
n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

d = [(1,0),(-1,0),(0,1),(0,-1)]

result = 0

safeZone = []
dangerZone = []

# BFS를 진행한후 0의 갯수를 파악한다. (시작위치는 2인 지역)
def BFS(newGraph):
    queue = deque()
    global result
    for dZone in dangerZone:
        queue.append(dZone)
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and newGraph[nx][ny] == 0:
                newGraph[nx][ny] = 2
                queue.append((nx,ny))
    
    count = 0

    for arry in newGraph:
        count += arry.count(0)
    
    result = max(count,result)

# 0인 지역과 2인 지역을 파악한다.
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
           safeZone.append((i,j))
        if graph[i][j] == 2:
            dangerZone.append((i,j))

# 벽을 3개 세운다.(0인 지역에)
walls = combinations(safeZone,3)

for wall1,wall2,wall3 in walls:
    newGraph = deepcopy(graph)
    newGraph[wall1[0]][wall1[1]] = 1
    newGraph[wall2[0]][wall2[1]] = 1
    newGraph[wall3[0]][wall3[1]] = 1
    BFS(newGraph)

print(result)
