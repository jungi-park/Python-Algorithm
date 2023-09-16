'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다.
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''
n=int(input())
time=[]

result=[]
for x in range(n):
    start,end=map(int,input().split())
    time.append([start,end])

'''
end와 start를 기준으로 정렬하는 아이디어를 떠올려야 한다
먼저 끝날 수록, 이후 시간에 예약할 수 있는 여유가 많아진다 : end 기준 정렬
끝나는 시각이 같을 때, 발생할 수 있는 예외에 대해서 고려해야 한다: start 기준 정렬
ex) 입력값이 n = 2, start, end = [(2 2), (1 2)] 일 때​
end, start 기준 정렬했을 때 time = [(1 2), (2 2)] : cnt = 2
​end 기준 정렬만 이용한다면 time = [(2 2), (1 2)] : cnt = 1
'''
time=sorted(time,key=lambda x:x[0])

time=sorted(time,key=lambda x:x[1])

cnt = 0
last_end=0

for start, end in time:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)
