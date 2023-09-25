n, m, v = map(int, input().split()) # node, edge, start_node
graph = [[] for i in range(n+1)]
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for j in range(n+1):
    graph[j].sort()
# print(graph)

def DFS(graph, v, visited):
    visited[v]=True 
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            DFS(graph, i, visited)

from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]==True:
                queue.append(i)
                visited[i]=True


visited = [False] * (n+1)
DFS(graph, v, visited)
print()
visited = [False] * (n+1)
BFS(graph, v, visited)