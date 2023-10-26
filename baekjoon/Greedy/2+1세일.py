n = int(input())

price = [int(input()) for _ in range(n)]

price.sort(reverse=True)

result = 0

for i in range(int(n//3)):
    result += price[3*i]+price[3*i+1]

for i in range(1,int(n%3)+1):
    result += price[-i]

for i in range(n):
    if i%3!=2:
        result += price[i]

print(result)