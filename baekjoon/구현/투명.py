n, m = map(int, input().split())
array = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for k in range(x1, x2+1):
        for l in range(y1, y2+1):
            array[k][l] += 1

for i in range(101):
    for j in range(101):
        if array[i][j] > m:
            result += 1

print(result)