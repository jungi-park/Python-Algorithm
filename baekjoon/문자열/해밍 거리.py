t = int(input())
result = [0 for _ in range(t)]
for i in range(t):
    a = list(map(str,input()))
    b = list(map(str,input()))

    for k in range(len(a)):
        if a[k] != b[k]:
            result[i] += 1

for j in result:
    print("Hamming distance is "+ str(j) +".")