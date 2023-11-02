n = int(input())
lost = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

# dp[i][j]는 i번째 사람까지 고려했을 때, 체력이 j일 때 얻을 수 있는 최대 기쁨을 나타냅니다. 
'''
즉 1번쨰 사람의 잃는량이 20 이고 행복량이 40일떄
dp[1][21]부터는  max(dp[i-1][j], dp[i-1][j-l] + h)
위의 코드가 실행된다.
2번쨰 사람의 잃는량이 20 이고 행복량이 40일떄
dp[2][21]일때 dp[1][21]과 dp[1][1] + h 중 큰값이 선택된다
'''
dp = [[0]*101 for _ in range(n+1)]

for i in range(1, n+1):
    l, h = lost[i], happy[i]
    for j in range(1, 101):
        if j < l:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l] + h)
            
print(dp[n][100])