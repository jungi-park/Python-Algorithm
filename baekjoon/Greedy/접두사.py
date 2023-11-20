n = int(input())

array = []

for _ in range(n):
  array.append(input())

array.sort(key=len)

result = 0

for i in range(n):
  for j in range(i+1,n):
    if array[i] == array[j][:len(array[i])]:
      result +=1
      break

print(n-result)

