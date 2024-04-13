people = 0
result = 0
for i in range(4):
    outP,inP = map(int,input().split())

    people -= outP
    people += inP
    result = max(result,people)

print(result)