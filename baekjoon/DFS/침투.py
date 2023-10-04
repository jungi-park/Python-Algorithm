import sys
sys.setrecursionlimit(10**9)
M,N = map(int,input().split())
graph=[list(map(int,input())) for _ in range(M)]

d =[(1,0),(-1,0),(0,1),(0,-1)]


def DFS (x,y):
    graph[x][y] = 2
    for dx,dy in d:
        nx = x+dx
        ny = y+dy

        if 0>nx or nx>=M or 0>ny or ny>=N:
            continue
        if graph[nx][ny] == 0:
            DFS(nx,ny)
 


for i in range(N):
    if graph[0][i] == 0:
        DFS(0,i)

if 2 in graph[-1] : print("YES")
else: print("NO") 