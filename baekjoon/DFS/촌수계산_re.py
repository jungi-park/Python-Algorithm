n = int(input())

start,end = map(int,input().split())

releation = int(input())

visited = set()

graph = [ [] for _ in range(n+1)]

for _ in range(releation):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

result = -1
def DFS(start,end,count):
    global result
    if start == end:
        result = count
        return
    for Gend in graph[start]:
        if (start,Gend) not in visited and (Gend,start) not in visited:
            visited.add((start,Gend))
            visited.add((Gend,start))
            DFS(Gend,end,count+1)

DFS(start,end,0)

print(result)