n = list(map(str,input()))

for i in range(len(n)-1,0,-1):
    if int(n[i])>4:
        n[i-1] = str(int(n[i-1])+1)
    n[i] = '0'

print(int("".join(n)))