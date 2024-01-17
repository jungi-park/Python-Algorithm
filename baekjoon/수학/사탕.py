n = int(input())

candy = []
result = []
for i in range(n):
  candy.append(int(input()))



def findZero (candy):
  result = 0
  if len(candy) % 2 == 1:
    for i,val in enumerate(candy):
      if i%2 == 0:
        result +=val
      else:
        result -=val
  else:
     for i,val in enumerate(candy):
      if i%2 == 0:
        result -=val
      else:
        result +=val

  return int(result/2)

result.append(findZero(candy))

for index in range(len(candy)-1):
  result.append(candy[index]-result[index])

for val in result:
  print(val)