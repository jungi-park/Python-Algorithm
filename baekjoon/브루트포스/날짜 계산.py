E,S,M = map(int,input().split())
nE,nS,nM = 1, 1, 1
result = 1
while True:
    
    if nE == E and nS == S and nM == M:
        break

    nE+=1
    nS+=1
    nM+=1
    result+=1

    if nE > 15:
        nE = 1
        
    if nS > 28:
        nS = 1

    if nM > 19:
        nM = 1




print(result)