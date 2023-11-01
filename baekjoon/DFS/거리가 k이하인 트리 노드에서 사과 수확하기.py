import sys
sys.setrecursionlimit(10**6)
n,k = map(int,input().split())

grahp = [[] for _ in range(n)]
visited = [False]*n

for _ in range(n-1):
    x,y = map(int,input().split())
    grahp[x].append(y)
    grahp[y].append(x)

apples= list(map(int,input().split()))

result = 0

def DFS(sx,count):
    global result
    visited[sx] = True

    if count>k:
        return
    
    if apples[sx] == 1:
        result +=1

    for x in grahp[sx]:
        if not visited[x]:
            visited[x] = True
            DFS(x,count+1)

DFS(0,0)

print(result)