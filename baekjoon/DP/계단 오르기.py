n = int(input())  # 계단의 개수 입력 받기
scores = []  # 각 계단의 점수를 저장할 리스트

for _ in range(n):
    score = int(input())  # 각 계단의 점수 입력 받기
    scores.append(score)  # 리스트에 추가

# DP 테이블 초기화
dp = [0] * n
dp[0] = scores[0]  # 첫 번째 계단까지의 최댓값은 첫 번째 계단의 점수

# 두 번째 계단까지의 최댓값은 첫 번째 계단 점수와 두 번째 계단 점수의 합
if n > 1:
    dp[1] = scores[0] + scores[1]

# 세 번째 계단부터는 두 가지 선택지가 있음
# 1. 한 칸 전에서 올라온 경우: dp[i-2] + scores[i]
# 2. 두 칸 전에서 올라온 경우: dp[i-3] + scores[i-1] + scores[i]
# 두 경우 중 최댓값을 선택하여 dp[i]에 저장
for i in range(2, n):
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

# 마지막 계단까지의 최댓값 출력
print(dp[n-1])