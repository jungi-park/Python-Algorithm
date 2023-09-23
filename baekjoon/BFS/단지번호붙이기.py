n = int(input())

graph = [[]]


for i in range(n):
    graph.append([0]+list(map(int,input())))

#상하좌우
dx=[1,-1,0,0]
dy=[0,0,-1,1]

from collections import deque
def BFS(startX,startY):
    queue = deque([[startX,startY]])
    graph[startX][startY] = 0
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx,ny])
                count += 1
    return count
                        
        
result = []
for i in range(1,n+1):
    for k in range(1,n+1):
        if graph[i][k] == 1:
            result.append(BFS(i,k))

result.sort()

print(len(result))

for i in range(len(result)):
    print(result[i])



              

            


            

