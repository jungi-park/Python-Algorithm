a = input()
b = int(input())
a= int(a[:-2]+"00")
while True:
    if a % b ==0:
        break
    a+=1
print(str(a)[-2:])
