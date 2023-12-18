from collections import deque
d = [(1,0),(-1,0),(0,-1),(0,1)]
def solution(board):
    answer = -1
    start = []
    for x,b in enumerate(board):
        imsi = []
        for y,i in enumerate(b):
            if i == "R":
                start = [x,y]
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    answer = BFS(start,visited,board)
    return answer

def BFS(start,visited,graph):
    sx,sy = start
    queue = deque()
    queue.append([sx,sy,0])
    visited[sx][sy] = True
    
    while queue:
        x,y,cou = queue.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<= nx < len(graph) and 0<=ny<len(graph[0]) and not visited[nx][ny]:
                if graph[nx][ny] == "G":
                    return cou+1
                if graph[nx][ny] == ".":
                    visited[nx][ny] = True
                    queue.append([nx,ny,cou+1])
    return -1
    
    