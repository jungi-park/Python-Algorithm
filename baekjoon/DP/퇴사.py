n = int(input())

schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0]*(n+1)

for i in range(n):
    for j in range(i+schedule[i][0],n+1): #해당 일의 작업이 끝나는 날 부터 마지막 날까지 계산
        if dp[j] < dp[i]+schedule[i][1]:
            dp[j]=dp[i]+schedule[i][1]

print(max(dp))