n,k = map(int,input().split())

array = list(input())

#n은 길이 k는 거리
result = 0
for i in range(n):
  if array[i] == "P":
    a = 0
    # i-k가 0보다 작으면 안되고 i+k+1이 n보다 커서는 안된다
    for j in range(max(i-k,0),min(i+k+1,n)):
      if array[j] == "H":
        array[j] = "eat"
        result +=1 
        break



print(result)