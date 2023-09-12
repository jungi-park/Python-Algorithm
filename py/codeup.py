'''
#1번
print("문장")
#2번
print("문장1 문장2")
#3번
print("Hello")
print("World")
#4번
print("'Hello'")
#5번
print("\"Hello\"")
#6번
print("\"!@#$%^&*()'")
#7번
print("\"C:\Download\\'hello'.py\"")
#8번
print("print(\"Hello\\nWorld\")")
#9번
a = input()
print(a)
#10번
a = input()
print(a)
#11번
a = input()
a = float(a)
print(a)
#12번
a = input() 
b = input()
a=int(a)
b=int(b)
print(a)
print(b)
#13번
a = input() 
b = input()
print(b)
print(a)
#14번
a = input() 
a = float(a)
print(a)
print(a)
print(a)
#15번
a,b= input().split(" ")
print(a)
print(b)
#16번
a,b= input().split(" ")
print(b)
print(a)
#17번
a= input()
print(a,a,a)
#18번
a,b= input().split(":")
print(a,b,sep=':')
#19번
y, m, d = input().split('.')
print(d,m,y,sep="-")
#20번
p,b = input().split('-')
print(p,b,sep="")
#21번
s = input()
for c in s:
    print(c)
#22번
s = input()
print(s[:2])
print(s[2:4])
print(s[4:])
#23번
h,m,s = input().split(":")
print(m)
#24번
a,n = input().split(" ")
print(a,n,sep="")
#25번
a,b = input().split(" ")
a = int(a)
b = int(b)
#26번
a,b = input().split(" ")
a = float(a)
b = float(b)
print(a+b)
#27번
a= input()
a = int(a)
print('%x'% a)
#28번
a= input()
a = int(a)
print('%X'% a)
#29번
a= input()
a = int(a,16)
print('%o'% a)
#30번
a= input()
a= ord(a)
print(a)
#31번
a= chr(int(input()))
print(a)
#32번
a= int(input())
print(-a)
#33번
a= ord(input())
print(chr(a+1))
#34번
a,b= input().split(" ")
print(int(a)-int(b))
#35번
a,b= input().split(" ")
print(float(a)*float(b))
#36번
a,b= input().split(" ")
print(a*int(b))
#37번
n = input()
s = input()
print(int(n)*s)
#38번
a,b= input().split(" ")
print(int(a)**int(b))
#39번
a,b= input().split(" ")
print(float(a)**float(b))
#40번
a,b= input().split(" ")
print(int(a)//int(b))
#41번
a,b= input().split(" ")
print(int(a)%int(b))
#42번
a=input()
a=float(a)
print(format(a, ".2f") )
#43번
a,b= input().split(" ")
print(format(float(a)/float(b),".3f"))
#44번
a,b= input().split(" ")
a= int(a)
b= int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f"))
#45번
a, b, c = input().split()
a = int(a) 
b= int(b)
c= int(c)
print(a+b+c,format((a+b+c)/3,".2f"),sep=" ")
#46번
a= int(input())
print(a<<1) #이렇게 비트 연산을 하면 2*1 * a 와같다.
print(a<<2) #이렇게 비트 연산을 하면 2*2 * a 와같다.
print(a>>1) #이렇게 비트 연산을 하면 2*-1 * a 와같다.
print(a>>2) #이렇게 비트 연산을 하면 2*-2 * a 와같다.
#47번
a, b = input().split()
a = int(a)
b = int(b)
print(2**b*a)
#48번
a, b = input().split()
print(int(a)<int(b))
#49번
a, b = input().split()
print(int(a)==int(b))
#50번
a, b = input().split()
print(int(a)<=int(b))
#51번
a, b = input().split()
print(int(a)!=int(b))
#52번
n = int(input())
print(bool(n))
#53번
n = int(input())
print(not bool(n))
#54번
a, b = input().split()
print(bool(int(a)) and bool(int(b)))
#55번
a, b = input().split()
print(bool(int(a)) or bool(int(b)))
#56번
a, b = input().split()
print(bool(int(a)) != bool(int(b)))
#57번
a, b = input().split()
print(bool(int(a)) == bool(int(b)))
#58번
a, b = input().split()
print(not bool(int(a)) and not bool(int(b)))
#59번
a = int(input())
print(~a)
#60번
a,b = input().split()
print(int(a)&int(b))
#61번
a,b = input().split()
print(int(a)|int(b))
#62번
a,b = input().split()
print(int(a)^int(b))
#63번
a, b = input().split()
a = int(a) 
b = int(b)
print(a if(a>=b) else b)
#64번
a, b,c = input().split()
a = int(a) 
b = int(b)
c = int(c)
d = a if(a<b) else b
e = d if(d<c) else c
print(e)
#65번
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)
#66번
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a%2==0 :
  print("even")
else :
  print("odd") 
if b%2==0 :
  print("even")
else :
  print("odd") 
if c%2==0 :
  print("even")
else :
  print("odd") 
#67번
a= int(input())
if a<0:
    if a%2 ==0: print("A")
    else: print("B")
else:
    if a%2 ==0: print("C")
    else: print("D")
#68번
n= int(input())
if n>=90 :
  print('A')
else :
  if n>=70 :
    print('B')
  else :
    if n>=40 :
      print('C')
    else :
      print('D') 
#69번
n= input()
if n=="A" : print("best!!!")
elif n=="B" : print("good!!")
elif n=="C" : print("run!")
elif n=="D" : print("slowly~")
else: print("what?")
#70번
n= int(input())
if n//3==1 : print("spring")
elif n//3==2 : print("summer")
elif n//3==3 : print("fall")
else: print("winter")
#71번
while True:
  n= int(input())
  if n == 0 :
      break
  else:
      print(n)
#72번
n= int(input())

while True:
    if n == 1 : break
    else: 
       print(n)
       n = n-1
#73번
n= int(input())
while True:
    if n == 0 : break
    else: 
       n = n-1
       print(n)
#74번
n= ord(input())
a = ord("a")
while a <= n:
    print(chr(a))
    a=a+1
#75번
n = int(input())
for x in range(n+1):
    print(x)
#76번
n = int(input())
for i in range(n+1) :
  print(i)
#77번
n = int(input())
for x in range(1,n+1):
    if x%2==1: print(x)
#78번
while True:
    n = input()
    if n =="q":break
    else: print(n)
#79번 
n= int(input())
num =0 

for x in range(1,1000):
    num = num +x
    if num>=n : 
       print(x)
       break
#80번 
a,b= input().split()
a= int(a)
b= int(b)
for ax in range(1,a+1):
    for bx in range(1,b+1):
        print(ax,bx)
#81번 
n= int(input(),16)

for x in range(1,16):
   print("{:X}*{:X}={:X}".format(n,x,n*x))
#82번
n = int(input())

for x in range(1,n+1):
    if x%3==0: print("X",end=" ")
    else: print(x,end=" ")
#83번
r,g,b = input().split()
r = int(r)
g = int(g)
b = int(b)
result = 0

for rx in range(r):
    for gx in range(g):
        for bx in range(b):
            result = result +1
            print(rx,gx,bx)

print(result)
#84번
h, b, c, s = input().split()
h = float(h)
b = float(b)
c = float(c)
s = float(s)

result =  h*b*c*s/8/1024/1024
print(format(result,".1f"),"MB")
#85번
r,g,b = input().split()
r = float(r)
g = float(g)
b = float(b)

result =  r*g*b/8/1024/1024
print(format(result,".2f"),"MB")
#86번
n = int(input())
num = 0
sum = 0
while True: 
    num = num +1
    sum = sum +num
    if n<=sum:
        print(sum)
        break
#87번
n = int(input())
for x in range(1,n+1):
    if x%3==0:
        continue
    else: print(x,end=" ")
#88번
a,d,n = input().split()
a= int(a)
d= int(d)
n= int(n)


for x in range(n):
    sum= d*x

print(a+sum)
#89번
a,r,n = input().split()
a= int(a)
r= int(r)
n= int(n)

for x in range(n-1):
    a = a*r

print(a)
#90번
a,m,d,n = input().split()
a= int(a)
m= int(m)
d= int(d)
n= int(n)
for x in range(n-1):
    a = a*m+d

print(a)
#91번
a,b,c = input().split()
a= int(a)
b= int(b)
c= int(c)
d =1 

while d%a != 0 or d%b != 0 or d%c != 0:
    d += 1

print(d)
#92번
n = int(input()) 
a = input().split()
result =[]

for x in range(24):
    result.append(0)

for x in range(n):
    result[int(a[x])-1]+=1
    
print(result,end=" ")
#93번
n = int(input()) 
a = input().split()

for i in range(n-1, -1, -1) :
  print(a[i], end=' ')
#94번
n = int(input()) 
a = input().split()
result= 0

for x in range(n):
    if x == 0:
        result = int(a[x])
    else:
        if result> int(a[x]) :
            result = int(a[x])
print(result)
#95번
n = int(input())

pan = []

for i in range(20):
  pan.append([])
  for k in range(20):
    pan[i].append(0)

for i in range(n):
  x,y = input().split()
  pan[int(x)-1][int(y)-1] += 1

for i in pan:
  for x in i:
    print(x,end=" ")
  print()
#96번

pan = []
for i in range(20) :
  pan.append([])
  for j in range(20) : 
    pan[i].append(0)

for i in range(19) :
    a = input().split()
    for j in range(19) :
        pan[i+1][j+1] = int(a[j])

n= int(input())

for i in range(n):
  x,y = input().split()
  x=int(x)
  y=int(y)
  
  for k in range(1,20):
    if pan[x][k] == 1 : pan[x][k]=0
    else: pan[x][k]=1
  
  for j in range(1,20):
    if pan[j][y] ==1 : pan[j][y]=0
    else: pan[j][y]=1

for i in range(1, 20) : 
    for j in range(1, 20) : 
        print(pan[i][j], end=' ') 
    print()
#97번
a,b=input().split()
h=int(a)
w=int(b)

m=[]
for i in range(h+1) :
    m.append([])
    for j in range(w+1) :
        m[i].append(0)

n=int(input())

for i in range(n) :
    l,d,x,y=input().split()
    for j in range(int(l)) :
        if int(d)==0 :
            m[int(x)][int(y)+j]=1
        else :
            m[int(x)+j][int(y)]=1


for i in range(1, h+1) :
    for j in range(1, w+1) :
        print(m[i][j], end=' ')
    print()
#98번
m=[]
for i in range(12) :
    m.append([])
    for j in range(12) :
        m[i].append(0)

for i in range(10) :
    a=input().split()
    for j in range(10) :
        m[i+1][j+1]=int(a[j])

x=2
y=2
while True :
    if m[x][y]==0 :
        m[x][y]=9
    elif m[x][y]==2 :
        m[x][y]=9
        break

    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
        break

    if m[x][y+1]!=1 :
        y+=1
    elif m[x+1][y]!=1 :
        x+=1
    

for i in range(1, 11) :
    for j in range(1, 11) :
        print(m[i][j], end=' ')
    print()
'''