k = int(input())

dp = [[1, 0] for _ in range(k+1)]

# dp[0] = "A" 1, 0 
# dp[1] = "B" 0, 1
# dp[2] = "BA" 1,1
# dp[3] = "BAB" 1,2
# dp[4] = "BABBA" 2,3
# dp[5] = "BABBABAB" 3 5
# dp[6] = "BABBABABBABBA"5 8

for i in range(1,k+1):
    dp[i] = [dp[i-1][1],dp[i-1][0]+dp[i-1][1]]

print(dp[k][0],dp[k][1])