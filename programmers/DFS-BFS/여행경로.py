from collections import deque
# 채점 결과
# 정확성: 50.0
# 합계: 50.0 / 100.0
def solution(tickets):
    answer = []
    graph = {}
    visited = set()
    queue = deque()

    for ticket in tickets:
        start, end = ticket
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = []
            graph[start].append(end) 

    queue.append("ICN")
    while queue:
        s = queue.popleft()
        if s in graph:
            for end in sorted(graph[s]):
                if (s, end) not in visited:
                    queue.append(end)
                    visited.add((s, end))
        answer.append(s)
    
    return answer