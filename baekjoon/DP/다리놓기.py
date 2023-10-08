T = int(input())
dp = [[0] * 30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(T):
    N, M = list(map(int, input().split()))
    print (dp[N][M])

#생각했지만 함수를 몰라서 못했던 풀이
import math
t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' '))
    print(math.comb(m, n))

