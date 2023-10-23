def search(x, y, pre, oper):
    global MIN, MAX
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if puzzle[nx][ny] == '+':
                search(nx, ny, pre, '+')
            elif puzzle[nx][ny] == '-':
                search(nx, ny, pre, '-')
            elif puzzle[nx][ny] == '*':
                search(nx, ny, pre, '*')
            else:
                if oper == '+': re = pre + int(puzzle[nx][ny])
                elif oper == '-': re = pre - int(puzzle[nx][ny])
                elif oper == '*': re = pre * int(puzzle[nx][ny])
                if nx == n-1 and ny == n-1:
                    MIN = min(MIN, re)
                    MAX = max(MAX, re)
                    return
                search(nx, ny, re, '')

n = int(input())
puzzle = []
for i in range(n):
    puzzle.append(input().split())
dx = [1, 0]
dy = [0, 1]
MIN, MAX = int(1e9), -int(1e9)
search(0, 0, int(puzzle[0][0]), '')
print(MAX, MIN)