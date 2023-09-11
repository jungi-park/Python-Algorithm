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
'''

