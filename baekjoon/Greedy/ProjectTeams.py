n = int(input())

stu = list(map(int,input().split()))

stu.sort()

result = float("inf")

for i in range(int(n)):
    result = min(result, stu[i]+stu[2*n-1-i])

print(result)