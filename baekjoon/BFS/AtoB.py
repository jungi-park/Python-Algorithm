a,b = map(int,input().split())

visited = {}

from collections import deque
def BFS():
    queue = deque()
    queue.append(a)
    visited[a] = 1
    while queue:
        s = queue.popleft()
        if s == b:
            return visited[s]
        if s*2<=b :
            if s*2 not in visited :
                visited[s*2] = visited[s]+1
                queue.append(s*2)
        if s*10 + 1<=b :
            if s*10 + 1 not in visited:
                visited[s*10 + 1] = visited[s]+1
                queue.append(s*10 + 1)
    return -1

print(BFS())