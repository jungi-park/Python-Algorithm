graph = [list(map(str,input().split())) for _ in range(5)]

result = set()

d = [(1,0),(-1,0),(0,1),(0,-1)]

def DFS(x,y,count,path):
    if count == 6 : 
        result.add(path)
        return
    path += graph[x][y]
    for dx,dy in d:
        nx = x + dx
        ny = y + dy
        if 0<=nx<5 and 0<=ny<5:
            DFS(nx,ny,count+1,path)


for i in range(5):
    for j in range(5):
        DFS(i,j,0,"")

print(len(result))