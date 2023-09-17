
'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
'''
s = int(input())

n=0

k= 1
while s !=0:
    if s-k>=0:
        if s-k > k:
            n =n+1
            s = s- k
            k=k+1
        elif s-k == 0:
            n =n+1
            s = s- k
        else:
            k=k+1


print(n)
