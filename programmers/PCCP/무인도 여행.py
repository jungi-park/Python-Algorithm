from collections import deque
d = [(1,0),(-1,0),(0,-1),(0,1)]
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for x,onemap in enumerate(maps):
        for y,i in enumerate(onemap):
            if i !="X" and not visited[x][y]:
                answer.append(BFS(x,y,maps,visited))
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer

def BFS(sx,sy,maps,visited):
    queue = deque()
    queue.append([sx,sy])
    count = 0
    visited[sx][sy] =True
    while queue:
        x,y = queue.popleft()
        count += int(maps[x][y])
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<len(maps) and 0<= ny <len(maps[0]) and not visited[nx][ny] and maps[nx][ny] !="X":
                queue.append([nx,ny])
                visited[nx][ny] =True
    return count
                
    