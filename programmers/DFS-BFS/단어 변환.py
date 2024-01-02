from collections import deque 
def solution(begin, target, words):
    answer = 0
    visited = set()
    answer = BFS(begin,target,visited,words)
    return answer

def BFS(begin,target,visited,words):
    q = deque()
    q.append([begin,0])
    while q :
        word,cnt = q.popleft()
        if word in visited:
            continue
        visited.add(word)
        if word == target:
            return cnt
        for i in range(len(words)):
            diff = 0
            for j in range(len(word)):
                if word[j] != words[i][j]:
                    diff += 1
            if diff == 1:
                q.append([words[i],cnt+1])
    return 0