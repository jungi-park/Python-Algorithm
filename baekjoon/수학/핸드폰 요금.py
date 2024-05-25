N = int(input())

fees = list(map(int,input().split()))

M = 0
Y = 0


def calM(fee):
    result = 0
    result+= 15*(fee//60 + 1)
    return result

def calY(fee):
    result = 0
    result+= 10*(fee//30 + 1)
    return result


for fee in fees:
    M += calM(fee)
    Y += calY(fee)

if M < Y:
    print("M " + str(M))
elif M == Y:
    print("Y M " + str(Y))
else:
    print("Y " + str(Y))