n,m = map(int,input().split())
j = int(input())

left = 1
right = m
result = 0

for i in range(j):
    p = int(input())
    if(left<=p<=right):
        result = result
    elif(right<p):
        result += p-right
        right = p
        left = right-m+1
    elif(p<left):
        result += left-p
        left = p
        right = left+m-1

print(result)