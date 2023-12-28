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