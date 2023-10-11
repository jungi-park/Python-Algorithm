n = int(input())

array = []
dp = []

for _ in range(n):
    array.append(list(map(int,input().split())))
    dp.append([1001]*3)

dp[0] = array[0]

for k in range(1, n):
    for j in range(3):
        if j == 0:
            dp[k][j] = min(dp[k-1][j+1]+array[k][j], dp[k-1][j+2]+array[k][j])
        elif j == 1:
            dp[k][j] = min(dp[k-1][j-1]+array[k][j], dp[k-1][j+1]+array[k][j])
        elif j == 2:
            dp[k][j] = min(dp[k-1][j-2]+array[k][j], dp[k-1][j-1]+array[k][j])

print(min(dp[n - 1]))
