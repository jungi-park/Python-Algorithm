a,b = map(int,input().split())

aSet = set(map(int,input().split()))
bSet = set(map(int,input().split()))

if sorted(aSet - bSet):
  print(len(sorted(aSet - bSet)))
  print(*sorted(aSet - bSet))
else:
  print(len(sorted(aSet - bSet)))