n = int(input())
result = 0
for i in range(1,n+1):
  strNum = list(map(int,str(i)))
  count  = 0
  diff = 0
  while count <= len(strNum)-1:
    if count == len(strNum)-1 :
      result+=1
      break
    if len(strNum) == 1:
      result+=1
      break
    elif count == 0:
      diff = int(strNum[count]) - int(strNum[count+1])
      count+=1
    else:
      if diff != int(strNum[count]) - int(strNum[count+1]):
        break
      count+=1
  
  

print(result)