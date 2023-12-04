from collections import deque
def solution(n, edge):
    answer = 0
    grahp =[[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    for x,y in edge:
        grahp[x].append(y)
        grahp[y].append(x)
    result = BFS(grahp,visited)
    return result.count(max(result))

def BFS(grahp,visited):
    queue = deque()
    queue.append([1,0])
    visited[1] = True
    result=[]
    
    while queue:
        x,coun = queue.popleft()
        result.append(coun)
        
        for y in grahp[x]:
            if visited[y] == False:
                visited[y] = True
                queue.append([y,coun+1])
    return result
        