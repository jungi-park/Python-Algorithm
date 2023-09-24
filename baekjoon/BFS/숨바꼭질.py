n,k = map(int,input().split())
MAX = 100000
visited = [0] * (MAX+1)


from collections import deque

def BFS():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break

        for j in (x-1,x+1,x*2):
            if 0<= j <= MAX and not visited[j]:
                visited[j] = visited[x] +1
                q.append(j)

BFS()
