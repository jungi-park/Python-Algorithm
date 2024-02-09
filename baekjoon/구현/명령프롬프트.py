n = int(input())

result = ""

for i in range(n):
    if i == 0:
        result = list(map(str,input()))
    else:
        l = list(map(str,input()))
        for k in range (len(result)):
            if l[k] == result[k]:
                pass
            else:
                result[k] = "?"

print(*result,sep="")