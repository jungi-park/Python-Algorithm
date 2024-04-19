n,k = map(int,input().split())

kids = list(map(int,input().split()))

diffArry = []

for i in range(n-1):
   diffArry.append(kids[i+1] - kids[i])
   
diffArry.sort(reverse=True)
print(sum(diffArry[k-1:]))

