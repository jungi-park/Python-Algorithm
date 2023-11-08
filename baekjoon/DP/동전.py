result = []
for _ in range(int(input())):
    n = int(input())
    coins = list(map(int,input().split()))
    money = int(input())
    dp = [0]*(money+1)
    '''
    dp[0]에 1을 넣는 이유는
    이는 어떤 동전이든 0원을 만들 수 있는 '가지수'는 무조건 1가지 존재한다는 의미이다. 생각해 보면 2원짜리 동전 0개로 0원을 만들 수 있다
    참조 https://d-cron.tistory.com/23
    '''
    dp[0] = 1
    for coin in coins:
        for i in range(money + 1):
            # a_(i-k) 를 만드는 방법이 존재한다면 
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
            if i >= coin:
                dp[i] += dp[i - coin]
    result.append(dp[money])

print(result)