n = int(input())

graph = dict()

for i in range(n):
    first,non,second = input().split()
    if first not in graph:
        graph[first] = [second]
    else:
        graph[first].append(second)

k = int(input())
result = ["F"] * k

def DFS(s,e,index):
    global result
    if s == e:
        result[index] = "T"
        return
    if s in graph:
        for se in graph[s]:
            DFS(se,e,index)

for index in range(k):
    first,non,second = input().split()
    DFS(first,second,index)
    print(result[index])