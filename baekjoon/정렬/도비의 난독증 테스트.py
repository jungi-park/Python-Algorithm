while True:
    n = int(input())
    if n == 0:
        break
    array = []
    for i in range(n):
        array.append(input())
    
    array.sort(key= lambda x :x.upper())
    print(array[0])