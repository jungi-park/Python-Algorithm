n = int(input())

# 시작,끝,인원 

meeting =[list(map(int,input().split())) for _ in range(n)]
meeting.sort(key=lambda x: x[1])  # 회의를 끝나는 시간을 기준으로 정렬

dp = [0] * n

for i in range(n):
  dp[i] = meeting[i][2]  # 현재 회의에 참석하는 인원 초기화
  for j in range(i):
    if meeting[i][0] >= meeting[j][1]:
      dp[i] = max(dp[i],dp[j]+meeting[i][2])


print(max(dp))