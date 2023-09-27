import sys

result = []
while True:
    w,h = map(int,sys.stdin.readline().split())

    if w == 0 and h ==0:
        for i in result:
            print(i)
        exit()

    graph= []
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))

    d = [(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1)]

    def DFS (startX,startY):
        stack = [(startX,startY)]
        
        while stack:
            x,y = stack.pop()
            graph[x][y] = 0
            
            for dx, dy in d:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                    stack.append((nx ,ny))
                    graph[nx][ny] = 0

    count = 0
    for i in range(h):
        for k in range(w):
            if graph[i][k] != 0:
                count +=1
                DFS(i,k)

    result.append(count)
