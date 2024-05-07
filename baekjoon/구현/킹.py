k,d,n = map(str,input().split())

sY ={"A":0,"B":1,"C":2,"D":3,"E":4,'F':5,"G":6,"H":7}

moveD = {"R":(0,1),"L":(0,-1),"B":(1,0),"T":(-1,0),"RT":(-1,1),"LT":(-1,-1),"RB":(1,1),"LB":(1,-1)}

kx = abs(int(k[1])-8)
ky = sY[k[0]]

ddx = abs(int(d[1])-8)
ddy = sY[d[0]]

board = [[0]*8 for _ in range(8)]


for i in range(int(n)):
    move = input()
    dx,dy = moveD[move]
    nkx = kx+dx
    nky = ky+dy
    if 0<=nkx<8 and 0<=nky<8:
        if nkx == ddx and nky == ddy:
            if 0<=ddy+dy<8 and 0<=ddx+dx<8:
                ddy += dy
                ddx += dx
                kx = nkx
                ky = nky
        else:
            kx = nkx
            ky = nky

for k in sY:
    if sY[k] == ky:
        print(k+str(abs(kx-8)))

for k in sY:
    if sY[k] == ddy:
        print(k+str(abs(ddx-8)))