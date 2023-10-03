import sys
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())

startP=[]
graph=[]
for i in range(n):
    inputD = input().strip()
    index = inputD.find("I")
    row = list(map(str,inputD))
    graph.append(row)
    if index != -1:
        startP.append((i,index))

d = [(1,0),(-1,0),(0,-1),(0,1)]

result = 0
def DFS(x,y):
    global result
    if graph[x][y] == "P":
        result +=1
    graph[x][y] = "X"
    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[nx][ny] != "X":
            DFS(nx,ny)

x,y = startP.pop()
DFS(x,y)
if result == 0 : result = "TT"
print(result)