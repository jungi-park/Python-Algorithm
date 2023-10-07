'''
다이나믹 프로그래밍
메모리를 적절히 사용하여 시간효율성을 비약적으로 향상시키는 방법
이미 계산된 문제는 별도의 영역에 저장하여 다시 계산하지 않도록함
일반적으로 탑다운,바텀업 으로 구성됨

다음조건 만족시 사용가능 
1. 최적부분구조 -  큰문제를 작은문제로 나눌수 있으며 답을모아 큰문제를 해결할 수 있을때
2. 중복되는 부분 문제 - 동일한 문제를 반복적으로 해결해야될때

메모제이션 
다이나믹 프로그래밍을 구현하는 방법중 하나로
한 번 계산한 결과를 메모리 공간에 메모하는 기법
캐싱이라고도함

탑다운 VS 바텀업
탑다운(메모제이션) 방식은 하향식이라고도하며 바텀업은 상향식이라고도함
다이나믹 프로그래밍의 전형적인 형태는 바텀업 방식이다.
결과 저장용 리스트는 DP테이블이라고 부릅니다.
엄밀히 말하면 메모리제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념

다이나믹 프로그래밍 VS 분할 정복
다이나믹 프로그래밍과 분할정복의 차이점은 부분문제의 중복입니다.
'''

#개미전사

# n = int(input())

# result = 0

# array = list(map(int,input().split()))
# #DP테이블 초기화
# d =[0]*100
# #다이나믹 프로그래밍 진행
# d[0] = array[0]
# d[1] = max(array[0],array[1])
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2]+array[i])

# print(d[n-1])

#1로 만들기

# n = int(input())
# # #DP테이블 초기화
# d = [0] *30001
# # #다이나믹 프로그래밍 진행
# for i in range(2,n+1):
#     #현재수에서 1을 빼는경우
#     d[i] = d[i-1]+1
#     #현재수가 2로 나누어 떨어지는 경우
#     if i%2 == 0:
#         d[i] = min(d[i],d[i//2]+1)
#     #현재수가 3로 나누어 떨어지는 경우
#     if i%3 == 0:
#         d[i] = min(d[i],d[i//3]+1)
#     #현재수가 5로 나누어 떨어지는 경우
#     if i%5== 0:
#         d[i] = min(d[i],d[i//5]+1)

# print(d[n])

#효율적인 화폐구성

# n,m = map(int,input().split())

# array= []

# #n개의 화폐 단위 입력
# for _ in range(n):
#     array.append(int(input()))
    

# d = [10001]*(m+1)

# d[0] = 0

# for i in range(n):
#     for j in range(array[i],m+1):
#         if d[j -array[i]] != 10001:
#             d[j] = min(d[j],d[j-array[i]+1])

# if d[m] == 10001:
#     print(-1)
# else:print(d[m])

#금광

for tc in range(int(input())):

    n,m = map(int,input().split())

    array = list(map(int,input().split()))

    dp = []

    for i in range(n):
        dp.append(array[i*m: i*m+m])
    #다이나믹 프로그래밍 진행
    for j in range(1,m): #열
        for i in range(n): #행
            #왼쪽위에서 오는경우
            if i == 0: left_up=0 #i == 0인경우 위에서 올 수 없어서 처리
            else:left_up = dp[i-1][j-1]
            #왼쪽아래에서 오는경우
            if i == n-1: left_down=0
            else:left_down = dp[i+1][j-1]
            #왼쪽에서 오는경우
            left =dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)
