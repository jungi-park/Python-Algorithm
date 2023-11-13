for _ in range(int(input())):
    n = int(input())
    s = list(map(str,input()))
    e = list(map(str,input()))
    cnt = []
    for i in range(n):
        if s[i] != e[i]:
                cnt.append(s[i])
    if not cnt: print(0)
    elif cnt.count("B") >= cnt.count("W"):print(cnt.count("B"))
    elif cnt.count("B") < cnt.count("W"):print(cnt.count("W"))