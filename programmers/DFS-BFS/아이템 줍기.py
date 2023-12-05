from collections import deque
# 정확성: 72.1
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append([characterX, characterY, 0])
    visited = set([(characterX, characterY)])
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                visited.add((i, j))
    
    while queue:
        px, py, cut = queue.popleft()
        if px == itemX and py == itemY:
            return cut
        for dx, dy in d:
            nx = px + dx
            ny = py + dy
            if (nx, ny) in visited:
                continue
            for x1, y1, x2, y2 in rectangle:
                if x1 <= nx <= x2 and y1 <= ny <= y2 and (nx, ny) not in visited:
                    queue.append([nx, ny, cut + 1])
                    visited.add((nx, ny))
    
    return answer
