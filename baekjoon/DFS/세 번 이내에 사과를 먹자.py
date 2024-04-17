graph = [list(map(int,input().split())) for _ in range(5)]
r,c = map(int,input().split())
d = [(1,0),(-1,0),(0,1),(0,-1)]
result = 0

def DFS(sx, sy, move, apple):
    global result
    
    if move > 3:
        return
    
    if apple >= 2:
        result = 1
        return

    for dx, dy in d:
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < 5 and 0 <= ny < 5 and graph[nx][ny] != -1:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                DFS(nx, ny, move + 1, apple + 1)
                graph[nx][ny] = 1
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1
                DFS(nx, ny, move + 1, apple)
                graph[nx][ny] = 0


DFS(r, c, 0, 0)

print(result)


# 참고
# import sys

# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
# graph = [list(map(int, input().split())) for _ in range(5)]
# visited = [[False] * 5 for _ in range(5)]
# r, c = map(int, input().split())


# def dfs(y, x, depth, cnt):
#     visited[y][x] = True
#     if graph[y][x] == 1:
#         cnt += 1
#     if 2 <= cnt:
#         return 1
#     if 2 < depth:
#         visited[y][x] = False
#         return 0
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < 5 and 0 <= nx < 5:
#             if not visited[ny][nx] and graph[ny][nx] != -1:
#                 if dfs(ny, nx, depth + 1, cnt) == 1:
#                     return 1
#     visited[y][x] = False
#     return 0


# print(dfs(r, c, 0, 0))

