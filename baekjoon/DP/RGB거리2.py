# 1. 각 집의 색깔마다 더할 수 있는 최솟값을 더해나간다.(이전 집과 같은 색은 안됨)

# 2. 마지막 집과 첫번째 집의 색깔은 달라야 한다. 

# 3. 처음집 색깔을 미리 정해두고 dp를 구해 나가면 된다.

n = int(input())
rgb = []
ans = float("inf")
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp = [[float("inf"), float("inf"), float("inf")] for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)