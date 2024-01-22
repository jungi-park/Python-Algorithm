import math

oneX, oneY = map(int, input().split())
twoX, twoY = map(int, input().split())

x = oneX * twoY + twoX * oneY
y = twoY * oneY

gcd = math.gcd(x, y)  # 최대공약수 계산

x //= gcd  # x를 최대공약수로 나누기
y //= gcd  # y를 최대공약수로 나누기

print(x, y)