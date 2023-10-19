import sys
sys.setrecursionlimit(10 ** 8)
n,m,r = map(int,input().split())
graph = []

for _ in range(n+1):
    graph.append([])

for _ in range(m):
    x,y = map(int,input().split())
    graph[y].append(x)
    graph[x].append(y)

visited = [False]*(n+1)

result = [0]*(n+1)

conut = 1
def DFS(x):
    global conut 
    visited[x] = True
    result[conut] = x
    graph[x].sort(reverse=True)
    for i in graph[x]:
        if visited[i] == False:
            visited[i] = True
            conut +=1
            DFS(i)

DFS(r)

for i in result[1:]:
    print(i)