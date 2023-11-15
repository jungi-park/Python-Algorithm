a,b = map(int,input().split())
n =int(input())
distance = abs(a-b)

for i in range(n):
    s = int(input())
    if abs(s-b)+1 < distance:
        distance = abs(s-b)+1

print(distance)