t = int(input())

for _ in range(t):
    input()
    c,y,su,sa,f =map(int,input().split())
    b,gs,gc,w =map(int,input().split())

    dough = min(c//0.5,y//0.5,su//0.25,sa//0.0625,f//0.5625)
    # 팬케이크 토핑 개수 계산
    toppings = sum([b, gs // 30, gc // 25, w // 10])
    print(int(min(dough, toppings)))