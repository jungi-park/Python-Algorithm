n = int(input())

numArray = []
resultArry=[]

for i in range(n):
    numArray.append(list(map(int,input().split())))

for i in range(n):
    result = 0
    for j in range(5):
        for k in range(j+1,5):
            for r in range(k+1,5):
                result = max(result,int(str(numArray[i][j] + numArray[i][k] +numArray[i][r])[-1]))
    resultArry.append(result)

resultArry.reverse()
print(n-resultArry.index(max(resultArry)))