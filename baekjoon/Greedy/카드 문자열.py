for _ in range(int(input())):
    result =[]
    n = int(input())
    card = list(map(str,input().split()))
    for i in range(n):
        if i == 0:
            result.append(card[i])
        elif ord(card[i])<=ord(result[0]):
            result = [card[i]] + result
        else:
            result = result+ [card[i]]
    print("".join(result))