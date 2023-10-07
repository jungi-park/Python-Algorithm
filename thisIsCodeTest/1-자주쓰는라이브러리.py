result = sum([1,2,3,4,5])
print(result)

min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(max_result,min_result)

result = eval("(3+5)*7")
print(result)

result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4],reverse=True)
print(result)
print(reverse_result)

array = [('홍길동',35),('이순신',75),('아무개',50)]
result = sorted(array,key=lambda x:x[1],reverse=True)
print(result)

'''
itertools 사용
순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것 --> n*(n-1)*(n-2)...(n-r+1)
조합: 서도 다른 n개에서 순서에 상관없이 r개를 선택하는것  --> n*(n-1)*(n-2)...(n-r+1) / r!

순열과 조합 차이 예시
1. 대표 뽑기

순열) 4명 중 반장, 부반장을 뽑을 때 경우의 수

- 서로 다른 4명이고 반장, 부반장을 뽑는다 (순서o)

- ₄P₂

 

조합) 4명 중 대표를 2명 뽑을 때 경우의 수

- 서로 다른 4명이고 대표를 2명 뽑는다 (순서x)

- ₄C₂

2. 후보 2명, 유권자 6명일 때 - 무기명 투표, 기명 투표

중복순열) 기명 투표 (내가 A, 친구가 B뽑은 것과 / 친구가 A, 내가 B 뽑은 것은 다른 것)


중복조합) 무기명 투표 
'''
#permutations --> 순열이라는 의미
#combinations --> 조합이라는 의미
from itertools import combinations, count,permutations
data = ['A','B','C']
result = list(permutations(data,3))
print(result)

result = list(combinations(data,2))
print(result)

#중복 순열, 중복 조합
#중복 순열 --> product
#중복 조합 --> combinations_with_replacement
from collections import Counter

counter = Counter(["red","blue","greens","blue","blue"])
print(counter['blue'])
print(counter['greens'])
print(dict(counter))

#math
import math
#최대공약수 --> gcd() 이용 
print(math.gcd(21,14))
#최소공배수 --> a*b // math.gcd(a,b)
def lcm(a,b):
  return a*b / math.gcd(a,b)
print(lcm(21,14))