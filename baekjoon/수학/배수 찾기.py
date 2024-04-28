n = int(input())

while True:
    numStr = int(input())
    if numStr == 0:
        break

    if numStr%n != 0:
        text = str(numStr) + " is NOT a multiple of " + str(n) + "."
    else:
        text = str(numStr) + " is a multiple of " + str(n) + "."
        
    print(text)