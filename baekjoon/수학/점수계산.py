n = int(input())
array = list(map(int,input().split()))
result = 0
cont = 1
for i in array:
    if i == 1:
        result += cont
        cont+=1
    else:
        cont = 1

print(result)