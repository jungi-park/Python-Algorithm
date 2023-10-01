import sys

sys.setrecursionlimit(10**6) # 재귀 깊이 변경

m, n, k = map(int, input().split())

graph = [[False] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for sy in range(y1,y2):
        for sx in range(x1,x2):
                graph[sy][sx] = True

d = [(1,0),(-1,0),(0,-1),(0,1)]

countOne = 0

def DFS(x,y):
    global countOne
    graph[x][y] = True
    countOne += 1
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if nx >= m or ny >= n or nx < 0 or ny < 0:
            continue
        if not graph[nx][ny]:
            DFS(nx ,ny)
            

count = 0
result = []

for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            countOne = 0
            DFS(i ,j)
            count += 1
            result.append(countOne)

print(count)
print(sorted(result))
