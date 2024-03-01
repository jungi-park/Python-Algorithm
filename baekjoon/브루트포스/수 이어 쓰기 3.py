n = input()
numList = ""
for i in range(1,int(n)+1):
    numList += str(i)

print(numList.find(n)+1)