for _ in range(int(input())):
    n = int(input())
    namu = list(map(int,input().split()))
    namu.sort(reverse=True)
    result = 0
    for i in range(n-2):
        result = max(result, namu[i] - namu[i+2])
    print(result)