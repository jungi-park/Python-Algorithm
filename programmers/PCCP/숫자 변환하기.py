from collections import deque
def solution(x, y, n):
    answer = bfs(x,y,n)
    return answer

def bfs(x,y,n):
    visited = set()
    queue =deque()
    queue.append([x,0])
    visited.add(x)
    while queue:
        nx,cnt = queue.popleft()
        if nx == y :
            return cnt
        if nx+n not in visited and nx+n <= y:
            visited.add(nx+n)
            queue.append([nx+n,cnt+1])
        if nx*2 not in visited and nx*2 <= y:
            visited.add(nx*2)
            queue.append([nx*2,cnt+1])
        if nx*3 not in visited and nx*3 <= y:
            visited.add(nx*3)
            queue.append([nx*3,cnt+1])
    return -1
        