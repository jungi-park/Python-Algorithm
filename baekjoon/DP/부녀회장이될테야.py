result = []
for _ in range(int(input())):
    k = int(input())
    n = int(input())

    dp = []
    
    for y in range(k+1):
        dp.append([0]*(n+1))
        for i in range(1,n+1):
            if y == 0:
                dp[y][i] = i
            else:
                dp[y][i] = sum(dp[y-1][:i+1])
    result.append(dp[k][n])
    
for i in result:
    print(i)