n = int(input())

dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for y in range(len(dp[i])):
        if y == 0:
            dp[i][y] += dp[i-1][y]
        elif y == len(dp[i]) - 1:
            dp[i][y] += dp[i-1][y-1]
        else:
            dp[i][y] += max(dp[i-1][y], dp[i-1][y-1])

print(max(dp[n-1]))
