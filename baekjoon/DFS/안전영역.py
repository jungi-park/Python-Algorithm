import sys
from copy import deepcopy

n = int(sys.stdin.readline())

graph = []


for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


copyGraph = deepcopy(graph)

maxHight = 0

for i in graph:
    imsi = max(i)
    maxHight = max(imsi,maxHight)

d = [(1,0),(-1,0),(0,-1),(0,1)]

def DFS(startX,startY,hight):
    stack = [[startX,startY]]
    graph[startX][startY] = 0
    
    while stack:
        x,y = stack.pop()
        for dx,dy in d:
            nx =  x+ dx
            ny =  y+ dy
            
            if 0<= nx < n and 0<= ny < n:
                if graph[nx][ny] > hight:
                    graph[nx][ny] = 0
                    stack.append([nx,ny])

result = []
for y in range(maxHight):
    count = 0
    graph = deepcopy(copyGraph)
    for i in range(n):
        for k in range(n):
                if graph[i][k]> y:
                    count += 1
                    DFS(i,k,y)
    result.append(count)

print(max(result))
