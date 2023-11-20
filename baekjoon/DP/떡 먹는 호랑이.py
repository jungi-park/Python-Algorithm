d,k = map(int,input().split())

fibo =[1,1]

for _ in range(d-2):
  fibo.append(fibo[-1]+fibo[-2])

a = 1
found = False

while True:
    if (k - a * fibo[d-3]) % fibo[d-2] == 0:
        b = (k - a * fibo[d-3]) // fibo[d-2]
        found = True
        break
    a += 1

if found:
    print(a)
    print(b)
else:
    print("a와 b를 찾을 수 없습니다.")