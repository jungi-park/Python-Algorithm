n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

result = ""

def DFS(sx, sy, distance):
    global result
    if graph[sx][sy] == -1:
        result = "HaruHaru"
        return
    d = [(0, distance), (distance, 0)]
    for dx, dy in d:
        nx = sx + dx
        ny = sy + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
          visited[nx][ny] = True
          DFS(nx, ny, graph[nx][ny])

visited[0][0] = True
DFS(0, 0, graph[0][0])
if result == "":
    print("Hing")
else:
    print(result)
