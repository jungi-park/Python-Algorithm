import sys
from copy import deepcopy

n = int(sys.stdin.readline())

graph = []

for i in range(n):
    k = list(map(str,sys.stdin.readline()))
    k.remove("\n")
    graph.append(k)

graph1 = deepcopy(graph)

d = [(1,0),(-1,0),(0,-1),(0,1)]

from collections import deque
def nomal(stratX,startY):
    queue = deque()
    queue.append([stratX,startY])
    sWord = graph[stratX][startY]
    graph[stratX][startY] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+d[i][0] 
            ny = y+d[i][1]
            if 0<= nx <n and 0<= ny <n:
                if sWord == graph[nx][ny] and graph[nx][ny] != 0:
                    queue.append([nx,ny])
                    graph[nx][ny] = 0 

def diffent(stratX,startY):
    queue = deque()
    queue.append([stratX,startY])
    sWord = graph1[stratX][startY]
    graph1[stratX][startY] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+d[i][0] 
            ny = y+d[i][1]
            if 0<= nx <n and 0<= ny <n:
                if  graph1[nx][ny] != 0:
                    if sWord == "B":
                     if sWord == graph1[nx][ny]:
                            queue.append([nx,ny])
                            graph1[nx][ny] = 0 
                    else :
                        if graph1[nx][ny] != "B":
                            queue.append([nx,ny])
                            graph1[nx][ny] = 0 



count = 0 
count1 = 0 


for i in range(n):
    for k in range(n):
        if graph[i][k] != 0:
            count +=1
            nomal(i,k)

for i in range(n):
    for k in range(n):
        if graph1[i][k] != 0:
            count1 +=1
            diffent(i,k)

print(count,end=" ")
print(count1)


