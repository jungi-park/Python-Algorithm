from collections import deque

k = int(input())
w, h = map(int, input().split())

result = -1

graph = []

for i in range(h):
    graph.append(list(map(int, input().split())))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
hd = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
visited = set()

def BFS(k):
    qu = deque()
    qu.append([0, 0, 0, k])
    visited.add((0, 0, k))
    global result

    while qu:
        x, y, count, countH = qu.popleft()

        if x == h - 1 and y == w - 1:
            result = count
            break

        for hx, hy in hd:
            hnx = x + hx
            hny = y + hy

            if 0 <= hnx < h and 0 <= hny < w:
              if(hnx, hny, countH - 1) not in visited and countH > 0:
                if graph[hnx][hny] != 1:
                    visited.add((hnx, hny, countH - 1))
                    qu.append([hnx, hny, count + 1, countH - 1])

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < h and 0 <= ny < w:
              if (nx, ny, countH) not in visited:
                if graph[nx][ny] != 1:
                    visited.add((nx, ny, countH))
                    qu.append([nx, ny, count + 1, countH])


BFS(k)
print(result)