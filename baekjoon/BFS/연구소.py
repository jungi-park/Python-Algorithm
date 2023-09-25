import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[]]

for i in range(n):
    graph.append([0]+list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

safeZone = []
dangerZone = []

for i in range(1,n+1):
    for k in range(1,m+1):
        if graph[i][k] == 0:
            safeZone.append([i,k])
        if graph[i][k] == 2:
             dangerZone.append([i,k])

result = 0

from collections import deque
def BFS(graph):
    queue = deque(dangerZone)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= n and 0 < ny <= m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] == 2
                    queue.append([nx,ny])
    
    count = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if graph[i][j] == 0:
                count += 1
    
    result = max(count,result)
    

from itertools import combinations
from copy import deepcopy


def wall():
    safeZoneCombo = combinations(safeZone,3)
    for zones in safeZoneCombo:
        a,b,c = zones[0],zones[1],zones[2]

        temp_graph = deepcopy(graph)
        temp_graph[a[0]][a[1]] = 1
        temp_graph[b[0]][b[1]] = 1
        temp_graph[c[0]][c[1]] = 1
        BFS(temp_graph)

wall()

print(result)