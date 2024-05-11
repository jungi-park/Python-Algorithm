alps = ["A","B","C","D","E","F","G","H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

while True:
    result = 0
    a = input()

    if a == "#":
        break

    a = a.upper()
    for alp in alps:
        if alp in a:
            result += 1
    print(result)