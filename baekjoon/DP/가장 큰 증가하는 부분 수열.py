n = int(input())

array = list(map(int,input().split()))

dp = array[:]

for i in range(1,n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[j]+array[i],dp[i])

print(max(dp))