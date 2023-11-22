n,w = map(int,input().split())

graph = []

for _ in range(n):
  graph.append(int(input()))

coin = 0
flag =""
for i in range(n):
  if graph[i] <= graph[min(i+1,n-1)]:
    if flag !="+":
      coin = w//graph[i]
      w = w % graph[i]
    flag ="+"
  elif graph[i] > graph[min(i+1,n-1)]:
    if flag !="-":
      w += coin*graph[i]
      coin = 0
    flag ="-"
  
  if i == n-1:
    w += coin*graph[i]


print(w)