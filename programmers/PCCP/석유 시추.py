from collections import deque
d = [(1,0),(-1,0),(0,1),(0,-1)]
def solution(land):
    answer = 0
    horizonSize = len(land[0])
    verticalSize = len(land)
    for i in range(horizonSize):
        visited = set()
        answer = max(answer,BFS(i,land,visited,horizonSize,verticalSize))
    return answer



def BFS(horizon,land,visited,horizonSize,verticalSize):
    queue = deque()
    count = 0
    for i in range(verticalSize):
        if land[i][horizon] == 1:
            queue.append([i,horizon])
            visited.add((i,horizon))
    while queue:
        x,y = queue.popleft()
        count+=1
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<= nx < verticalSize and 0<= ny < horizonSize:
                if (nx,ny) not in visited and land[nx][ny] == 1:
                    queue.append([nx,ny])
                    visited.add((nx,ny))
    return count
        