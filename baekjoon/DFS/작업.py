import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[y].append(x)

x = int(input())


def DFS(sx):
    count = 0
    stack = [sx]
    visited[sx] = True
    while stack:
        dx = stack.pop()
        for x in graph[dx]:
            if visited[x] == False:
                visited[x] = True
                stack.append(x)
                count += 1
    return count

print(DFS(x))