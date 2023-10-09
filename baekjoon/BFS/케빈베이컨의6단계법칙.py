n,m= map(int,input().split())

graph = [[] for _ in range(n+1) ]

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


from collections import deque
def BFS(startX):
    visited = [False] *(n+1)
    count = [0] * (n+1)
    queue = deque()
    queue.append(startX)
    visited[startX] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                count[i] = count[x] + 1
                visited[i] = True
                queue.append(i)
    return sum(count)

    

result = []
for i in range(1,n+1):
    result.append(BFS(i))

print(result.index(min(result))+1)