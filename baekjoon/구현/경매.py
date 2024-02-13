u,n = map(int,input().split())

people = []
valCount = {}

for i in range(n):
  name,value = map(str,input().split())
  people.append([name,int(value)])
  if valCount.get(int(value)):
    valCount[int(value)] +=1
  else:
    valCount[int(value)] = 1

findValue = list(sorted(valCount.items(),key=lambda x : (x[1],x[0])))[0]

for name,value in people:
  if value == findValue[0]: 
    print(name,value)
    break