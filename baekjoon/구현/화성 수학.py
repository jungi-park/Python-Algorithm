T = int(input())

for _ in range(T):
    all = list(map(str,input().split()))
    num = float(all[0])
    operators = all[1:]
    for operator in operators:
        if operator == "@":
            num *= 3
        if operator == "%":
            num += 5
        if operator == "#":
            num -= 7
    f,n = str(num).split(".")
    if len(n)<2:
        n +="0"
    print(f+"."+n[:2])