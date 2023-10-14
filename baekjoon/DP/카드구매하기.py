n = int(input())

pay = [0]+ list(map(int,input().split()))

dp = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
            dp[i] = max(dp[i],pay[j] + dp[i-j])

print(dp[n])