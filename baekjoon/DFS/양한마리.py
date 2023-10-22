
import sys

sys.setrecursionlimit(10**6)

d = [(1,0),(-1,0),(0,1),(0,-1)]

result = []

def DFS(sx,sy):
    graph[sx][sy] = "."
    for dx,dy in d:
        nx = sx + dx
        ny = sy + dy

        if nx<0 or nx>= h or ny<0 or ny>=w:
            continue
        if graph[nx][ny] == "#":
            graph[nx][ny] = "."
            DFS(nx,ny)    
    

for _ in range(int(input())):
    h,w = map(int,input().split())

    graph = []

    for _ in range(h):
        graph.append(list(map(str,input().strip())))
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "#":
                count += 1
                DFS(i,j)
    result.append(count)

for i in result:
    print(i)