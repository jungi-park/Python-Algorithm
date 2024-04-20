# 내문제풀이
# n = int(input())

# assignments = [ list(map(int,input().split())) for _ in range(n)]

# assignments.sort(key=lambda x : (-x[1]))

# couurentDay = 0
# result = 0

# for endDay,socre in assignments:
#     if endDay > couurentDay:
#         result+=socre
#         couurentDay+=1


# print(result)

# 참고하여 푼 코드
n = int(input())
assignments = [ list(map(int,input().split())) for _ in range(n)]

assignments.sort(key=lambda x : (-x[1]))

assigned = [False]*1001
score = 0

# 여기가 핵심임 배정할 수 있는 날중 최대한 미루기 위한 코드
while assignments:
    # 가장 스코어 높은 순으로 가져와서
    d,w  = assignments.pop(0)

    # d일부터 1일 까지 거꾸로 돌면서 비어있는 날 중에 최대한 늦게 배정
    for i in range(d, 0, -1):
        if assigned[i]:
            continue

        assigned[i] = True
        score += w
        break

print(score)