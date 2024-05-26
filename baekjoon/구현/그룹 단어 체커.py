N = int(input())
result = 0
for _ in range(N):
    s = input()
    flag = True
    check = set()
    for index in range(1,len(s)):
        prevS = s[index-1]
        nowS = s[index]
        if nowS != prevS and nowS in check:
            flag = False
            break
        elif nowS != prevS:
            check.add(prevS)
    if flag:
        result += 1

print(result)