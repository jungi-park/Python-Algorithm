n =int(input())

cow = [list(map(int,input().split()))for _ in range(n)]

cow.sort(key=lambda x:x[0])

time = 0

for i in cow:
    arrive, delay = i
    if time > arrive:
        time += delay
    elif time <= arrive:
         time = arrive
         time += delay

print(time)
