x = int(input())

start = 64
kind = [64,32,16,8,4,2,1]
result = 0

while x != 0 :
  for i in kind:
    if x>=i:
      x-=i
      result+=1
      break

print(result)