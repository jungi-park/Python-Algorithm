n,m = map(int,input().split())

strNum = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

array =[]

for i in range(n,m+1):
  text =""
  for j in str(i):
    text += strNum[int(j)]
  array.append([text,i])

array.sort(key= lambda x: x[0])

for i,j in array:
  print(j)