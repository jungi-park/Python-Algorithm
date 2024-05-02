n = int(input())

road = list(map(int,input().split()))

diff = 0
result = -1
for roadIndex in range(len(road)-1) :
    if road[roadIndex] < road[roadIndex+1]:
        diff+= road[roadIndex+1]-road[roadIndex]
    else:
        result = max(result,diff)
        diff = 0
    if roadIndex == n-2:
        result = max(result,diff)

print(result)