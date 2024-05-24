from collections import deque

N =int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0]*(N+1)

def BFS():
    qu = deque()
    qu.append(1)
    while qu:
        s = qu.popleft()
        for e in graph[s]:
            if visited[e] == 0:
                visited[e] = s
                qu.append(e)

BFS()
for result in visited[2:]:
    print(result)