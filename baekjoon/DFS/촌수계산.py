n = int(input())
endX,startX = map(int,input().split())
m = int(input())

graph = [[]for _ in range(n+1)]
visited =[False]*(n+1)

for i in range(m):
    x,y =map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

result = []
def DFS(start,count):  
    visited[start] = True
    if start == endX: result.append(count)
    for i in graph[start]:
        if visited[i] == False:
            count+=1
            DFS(i,count)

DFS(startX,0)

if len(result)>0: print(result[0])
else: print(-1)