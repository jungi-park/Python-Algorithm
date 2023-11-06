import sys

sys.setrecursionlimit(10 ** 8)

r,c = map(int,input().split())

graph = [list(map(str,input())) for _ in range(r)]

d =[(1,0),(-1,0),(0,-1),(0,1)]



result = [0,0]

def DFS(sx,sy):
    ship=0
    wolf=0
    stack = []
    stack.append([sx,sy])
    if graph[sx][sy] =="v":
        wolf +=1
    if graph[sx][sy] =="k":
        ship +=1
    graph[sx][sy]="#"
    while stack:
        x,y = stack.pop()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] != "#":
                    if graph[nx][ny] =="v":
                        wolf +=1
                    if graph[nx][ny] =="k":
                        ship +=1
                    graph[nx][ny] = "#"
                    stack.append([nx,ny])
    if ship>wolf:
        result[0] = result[0]+ship
    else:
        result[1] = result[1]+wolf


for i in range(r):
    for j in range(c):
        if graph[i][j]=="v" or graph[i][j]=="k":
            DFS(i,j)

print(result[0],result[1])