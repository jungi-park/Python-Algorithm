n = int(input())
sList = []
for _ in range(n):
  sList.append(input())

sList.sort(key=lambda x : (len(x),sum([int(i) for i in x if i.isdigit()]),x))

for i in sList:
  print(i)