def solution(board, h, w):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    answer = 0
    
    for dx,dy in d:
        nx = h +dx
        ny = w +dy
        if 0<=nx<len(board) and 0<=ny<len(board[0]):
            if board[h][w] == board[nx][ny]:
                answer+=1
    return answer