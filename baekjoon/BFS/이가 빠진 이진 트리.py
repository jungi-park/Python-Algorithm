import sys

sys.setrecursionlimit(10 ** 8)

n = int(input())
order = list(map(int, input().split()))
order.remove(-1)
order.append(int(input()))
order.sort()
result = []


def DFS(arry):
    global result
    middle = int((len(arry) - 1) / 2)
    if len(arry) == 1:
        result.append(arry[0])
        return
    
    left = arry[:middle]
    right = arry[middle + 1:]
    
    DFS(left)
    DFS(right)
    result.append(arry[middle])

DFS(order)
for r in result:
    print(r,end=" ")