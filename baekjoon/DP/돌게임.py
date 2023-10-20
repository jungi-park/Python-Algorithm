n = int(input())

# 그럼 돌입장에서 1개를 가져 갈 수 있는턴은? 1
# 2개를 가져 갈 수 있는턴은 2
# 3개를 가져갈 수 있는 턴은 3 or 1
# 4개를 가져 갈 수 있는 턴은 4 or 2
# 5개를 가져 갈 수 있는 턴은 5 or 3
# 6개를 가져 갈수 있는턴은 6 or 4 or 2

# dp[n] = n, n-2.... >=1

anwser = n%2

if anwser == 0:
    print("CY")
else:
    print("SK")