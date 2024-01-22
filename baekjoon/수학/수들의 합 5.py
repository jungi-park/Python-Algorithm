n = int(input())

left =1
right =2
total = 1
result = 0

while right<=n and left<=right:
  
  if total<n:
    total+=right
    right+=1
  elif total >n:
    total-=left
    left+=1
  elif total == n:
    result+=1
    total+=right
    right+=1

print(result+1)
