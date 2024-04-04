w = list(map(int,input().split()))

ow = [1,1,2,2,2,8]

for i in range(len(w)):
    ow[i] = str(ow[i] - w[i])

print(" ".join(ow))