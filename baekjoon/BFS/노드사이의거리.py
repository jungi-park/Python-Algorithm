n,m = map(int,input().split())

graph = [[]]

for k in range(n):
    graph.append([])

for z in range(n-1):
    x,y,d= map(int,input().split())
    graph[x].append([y,d])
    graph[y].append([x,d])

result= []

from collections import deque

for _ in range(m):
    visited = [False] * (n+1)
    count = 0
    s,e = map(int,input().split())

    queue = deque()

    queue.append([s,0])

    visited[s] = True

    while queue:
        x,distance = queue.popleft()
        if x == e:
            result.append(distance)
            break
        for array in graph[x]:
            if visited[array[0]] == False:
                visited[array[0]] = True
                queue.append([array[0],distance+array[1]])

for i in result:
    print(i)