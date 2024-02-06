import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
answer = 0


def dfs(node, depth):
    global cnt, answer
    cnt += 1
    visited[node] = depth * cnt
    answer += visited[node]
    for i in sorted(graph[node], reverse=True):
        if visited[i] == -1:
            dfs(i, depth + 1)
    return


dfs(r, 0)
print(answer)