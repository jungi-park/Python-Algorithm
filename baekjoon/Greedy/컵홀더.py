n = int(input())
# seats = list(map(str,input()))
seats = input()
k = 0

seats = seats.replace("S","S*")
seats = seats.replace("LL","LL*")

seats = list(map(str,"*"+seats))

holder = seats.count("*")

if holder<n:
  print(holder)
else:
  print(n)