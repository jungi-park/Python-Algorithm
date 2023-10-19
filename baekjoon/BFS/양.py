n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(str,input().strip())))


from collections import deque

d = [(1,0),(-1,0),(0,-1),(0,1)]

result = [0,0]

def BFS(sx,sy):
    queue = deque()
    queue.append([sx,sy])
    ship = 0
    wolf =0
    if graph[sx][sy] == "v":
                    wolf += 1
    if graph[sx][sy] == "o":
                    ship += 1
    graph[sx][sy] ="#"
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            nx = x+ dx 
            ny = y+ dy
            if nx<0 or nx>= n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] != "#":
                queue.append([nx,ny])
                if graph[nx][ny] == "v":
                    wolf += 1
                if graph[nx][ny] == "o":
                    ship += 1
                graph[nx][ny] = "#"
    if wolf >= ship:
          result[1] += wolf
    else:
        result[0] += ship


for i in range(n):
    for j in range(m):
          if graph[i][j] != "#":
                BFS(i,j)

print(str(result[0]) +" "+ str(result[1]))