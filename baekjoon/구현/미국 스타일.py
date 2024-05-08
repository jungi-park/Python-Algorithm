T = int(input())

for _ in range(T):
    num,danwe = map(str,input().split())
    num = float(num)
    if danwe == "kg":
        num *= 2.2046
        print("%.4f lb" % (num))
    elif danwe == "lb":
        num *= 0.4536
        print("%.4f kg" % (num))
    elif danwe == "l":
        num *= 0.2642
        print("%.4f g" % (num))
    elif danwe == "g":
        num *= 3.7854
        print("%.4f l" % (num))