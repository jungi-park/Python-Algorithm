n,kim,im = map(int,input().split())
array = [0]*(n)
array[kim-1] = 1
array[im-1] = 1
count = 0
flag = True
while flag:
    imsi = []
    count+=1
    if len(array)//2 == 0:
        count = -1
        break
    for i in range(len(array)//2):
        if array[i*2] == 1 and array[i*2+1] == 1:
            flag = False
        elif array[i*2] == 1 or array[i*2+1] == 1:
           imsi.append(1)
        else:
            imsi.append(0) 
    if len(array)%2 != 0:
        imsi.append(array[-1])
    array = imsi

print(count)
