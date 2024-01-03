# 내 문제풀이 BFS 이용 -> 효율성 테스트 실패
from collections import deque
d = [(0,1),(1,0)]
def solution(m, n, puddles):
    answer = 0
    graph = [[0]*(m+1) for _ in range(n+1)]
    for g,s in puddles:
        graph[s][g] = 1
        
    answer = len(BFS(m,n,graph))%1000000007
    
    return answer

def BFS(m,n,graph):
    q = deque()
    q.append([1,1,0])
    graph[1][1] = 1
    result = []
    while q:
        x,y,cnt = q.popleft()
        if x ==n and y==m:
            result.append(cnt)
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<nx<=n and 0<ny<=m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append([nx,ny,cnt+1])
                    graph[nx][ny] = 0
    return result

# 인터넷 참고 DP 이용
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)] # dp 테이블 초기화
    dp[1][1] = 1
    
    for i, j in puddles: # 웅덩이가 있는 곳은 -1로 표시
        dp[j][i] = -1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1: # 웅덩이이면
                dp[i][j] = 0 # 이후 값에 영향을 주지 않게 하기 위해 0으로 바꾸고
                continue # 건너뜀
                
            # 위에서 오는 경우와 왼쪽에서 오는 경우를 더해줌
            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            
    return(dp[n][m])
                    
                
        