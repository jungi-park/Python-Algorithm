a,k = map(int,input().split())

from collections import deque

visited = [False]* 1000001

def BFS():
    queue = deque()
    queue.append([a,0])
    visited[a] = True 
    while queue:
        x,count = queue.popleft()
        if x == k :
            return count
        if x+1 <=k and visited[x+1] == False:
            visited[x+1] = True
            queue.append([x+1,count+1])
        if x*2 <=k and visited[x*2] == False:
            visited[x*2] = True
            queue.append([x*2,count+1])

print(BFS())