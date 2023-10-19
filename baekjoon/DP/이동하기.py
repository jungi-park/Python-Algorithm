n,m = map(int,input().split())

graph = []
dp = []

d = [(1,0),(0,1),(1,1)]

for _ in range(n):
    graph.append(list(map(int,input().split())))
    dp.append([0]*m)



for i in range(n):
    for j in range(m):
        if i== 0 and j ==0:
            dp[i][j] = graph[i][j]
        else:
           maxVal = max(dp[i-dx][j-dy] for dx,dy in d if i-dx>=0 and j-dy>=0)
           dp[i][j] = maxVal + graph[i][j]


print(dp[n-1][m-1])