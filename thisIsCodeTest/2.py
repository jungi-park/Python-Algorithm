'''
그리디 알고리즘
현재 상황에서 당장 좋은것만 고르는방법

그리디 해법은 그 정당성 분석이 중요하다
즉, 단순히 가장 좋은것만 반복적으로 선택해도 최적의 해를 구할 수 있는지 판단하는 것이 중요함

일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을때가 많습니다.



#거스름돈 문제
n=int(input())
result = 0

array = [500,100,50,10]

for coin in array:
    result = result+ n//coin
    n = n%coin

print(result)

#1이 될때까지
n,k=input().split()
n=int(n)
k=int(k)

count = 0


while n != 1:
    if n%k == 0 :
        n=n/k
        count +=1
    else:
        n=n-1
        count +=1

print(count)
#곱하기 혹은 더하기
n = input()
result = int(n[0])

for num in range(1,len(n)):
    if  int(n[num]) <= 1 or result<= 1:
        result+= int(n[num]) 
    else:
        result*= int(n[num]) 

print(result)        
#모험가 길드
all = int(input())
man = input().split()
sortMan = sorted(man)

result = 0
panding = []

for oneMan in sortMan:
    one = int(oneMan)
    if one ==1:
        result+=1
    else:
      panding.append(int(oneMan))
      if len(panding) == max(panding):
         result+=1
         panding=[]

print(result)
#상하좌우
n = int(input())
plan = input().split()

startX = 1
startY = 1

for direction in plan:
    if direction == "R":
        if startY+1 <= n:
            startY += 1
    if direction == "L":
        if startY-1 >= 1:
            startY -= 1
    if direction == "U":
        if startX-1 >= 1:
            startX -= 1
    if direction == "D":
        if startX+1 <= n:
            startX += 1
print(startX,startY)
#시각
n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h)+str(m)+str(s):
                count +=1

print(count)
#왕실의 나이트
n= input()
x=int(n[1])
y=ord(n[0]) - ord("a") +1
count = 0

if y+2<=8:
    if x+1<=8:
        count+=1
    if x-1 >0 :
        count+=1

if y-2>=1:
    if x+1<=8:
        count+=1
    if x-1 >0 :
        count+=1

if x+2<=8:
     if y+1<=8:
        count+=1
     if y-1 >0 :
        count+=1

if x-2>=1:
     if y+1<=8:
        count+=1
     if y-1 >0 :
        count+=1
print(count)
'''
#문자열 재정렬
n= input()
num=0
enArr=[]
for k in n:
    if ord(k)>=65:
        enArr.append(k)
    else:
        num += int(k)
result = sorted(enArr)
if num != 0:
    result.append(str(num))
# join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수입니다.
print("".join(result))

    






    
    
