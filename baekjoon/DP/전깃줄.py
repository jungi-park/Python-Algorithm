n = int(input())

line = [list(map(int,input().split()))for _ in range(n)]

line.sort(key=lambda x: x[0])
dp = [1]*n

for i in range(n):
    for j in range(i):
        # 겹친거 말고 안겹친걸 찾는거임
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(n - max(dp))