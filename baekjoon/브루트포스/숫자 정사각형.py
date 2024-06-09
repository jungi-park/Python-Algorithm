N,M = map(int,input().split())

graph = [list(map(int,input())) for _ in range(N)]
result = 1

for r in range(N):
    for c in range(M):
        d = 1
        while r+d<N and c+d<M:
            if graph[r][c] == graph[r][c+d] and graph[r][c] == graph[r+d][c] and graph[r][c] == graph[r+d][c+d]:
                result = max((d+1)**2,result)
            d += 1

print(result)