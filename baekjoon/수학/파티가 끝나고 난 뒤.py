l,p = map(int,input().split())

article = list(map(int,input().split()))

for i in range(len(article)):
   article[i] = str(article[i] - l*p)


print(" ".join(article)) 