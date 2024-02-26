x, y, w, h = map(int,input().split())
result = 0
d = [x,y,w-x ,h-y]
if d.index(min(d)) <= 1:
  while x != 0 and y != 0:
    x-=1
    y-=1 
    result+=1
else:
  while x != w and y != h:
    x+=1
    y+=1 
    result+=1

print(result)