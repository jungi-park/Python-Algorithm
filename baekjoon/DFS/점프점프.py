n = int(input())
a = [0]+list(map(int,input().split()))
s = int(input())
visited = [False]* (n+1)

def DFS():
    stack = []
    stack.append(s)
    visited[s] = True
    while stack:
        x = stack.pop()
        dis = a[x]
        if 0< x-dis and visited[x-dis] == False:
            stack.append(x-dis)
            visited[x-dis] = True
        if x+dis<=n and visited[x+dis] == False:
            stack.append(x+dis)
            visited[x+dis] = True
    return visited

print(DFS().count(True))