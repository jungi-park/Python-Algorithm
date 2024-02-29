def isYoon(y):
    isResult = False
    if y % 4 == 0:
        isResult =True
        if y % 100 == 0:
            isResult = False
            if y % 400 == 0:
                isResult = True
    return isResult

while True:
    d,m,y = map(int,input().split())
    if d == 0 and m == 0 and y ==0 :
        break
    result = 0

    yoon = isYoon(y)


    for i in range(1,m):
        day = 31
        if i == 2:
            if yoon:
                day = 29
            else:
                day = 28
        if i == 4 or i == 6 or i == 9 or i == 11:
            day =30
        result=result+ day

    print(result+d)