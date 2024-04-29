from collections import deque
n = int(input())

grahp = [[] for i in range(n)]

for k in range(n):
    for j in input():
        if j == "N":
            grahp[k].append(0)
        else:
            grahp[k].append(1)

result = 0

def BFS(index,visied,move=0):
    queue = deque()
    visied.add(index)
    queue.append((index,move))
    count = 0
    global result
    while queue:
        x,moveX = queue.popleft()
        for arrayIndex in range(len(grahp[x])):
            if grahp[x][arrayIndex] == 1 and arrayIndex not in visied and moveX+1 < 3:
                visied.add(arrayIndex)
                count+=1
                queue.append((arrayIndex,moveX+1))
    result = max(result,count)
    
for index in range(n):
    count = 0
    visied =set()
    BFS(index,visied,0)

print(result)