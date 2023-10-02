n,m = map(int,input().split())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

d = [(1,0),(-1,0),(0,-1),(0,1)]

result= []
def DFS(x,y):
    if x == n-1 and y == m-1:
        result.append(0)
        return
    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue 
        if graph[x][y] > graph[nx][ny]:
            DFS(nx,ny)

DFS(0,0)
print(len(result))