# 내답 시간초과
def solution(triangle):
  answer = 0
  def recur(i,j,exVal):
    dp[i] = max(dp[i],exVal+triangle[i][j])
    if i+1 < len(triangle):
      recur(i+1,j,exVal+triangle[i][j])
    if j+1 < len(triangle[i]):
      recur(i+1,j+1,exVal+triangle[i][j])
  dp = [0] * len(triangle)
  recur(0,0,0)
  answer=dp[len(triangle)-1]
  return answer

def solution(triangle):
    memo ={}
    def recur(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        if i == len(triangle)-1:
            return triangle[i][j]
        right = recur(i+1,j+1)
        down = recur(i+1,j)
        memo[(i,j)] = triangle[i][j] + max(right,down)
        return memo[(i,j)]
        
    recur(0,0)
    return memo[(0,0)]