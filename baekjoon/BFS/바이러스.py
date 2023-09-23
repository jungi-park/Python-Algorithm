n = int(input())
m = int(input())

graph=[]
visited = [False]*(n+1)
for i in range(n+1):
    graph.append([])

for i in range(m):
    x,y =map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

from collections import deque
def BFS(graph,start,visited):
    queue = deque([start])
    while queue:
        index = queue.popleft()
        visited[index] = True
        for i in graph[index]:
            if visited[i] == False:
                queue.append(i)
    return visited
    
                


print(BFS(graph,1,visited).count(True)-1)
    
