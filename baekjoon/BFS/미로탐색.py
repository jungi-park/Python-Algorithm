n,m = map(int,input().split())
graph=[[]]
for i in range(n):
    graph.append([0]+list(map(int,input())))


from collections import deque
def BFS(startX,startY):
    queue = deque([[startX,startY]])
    graph[startX][startY] = 0
    while queue:
       x,y= queue.popleft()
       if x+1 <= n and graph[x+1][y] == 1:
           queue.append([x+1,y])
           graph[x+1][y] = graph[x][y] +1
       if x-1 >=1 and graph[x-1][y] == 1:
           queue.append([x-1,y])
           graph[x-1][y] = graph[x][y] +1
       if y+1 <= m  and graph[x][y+1] == 1:
           queue.append([x,y+1])
           graph[x][y+1] = graph[x][y] +1
       if y-1 >=1  and graph[x][y-1] == 1:
           queue.append([x,y-1])
           graph[x][y-1] = graph[x][y] +1
    print(graph[n][m]+1)

BFS(1,1)