'''
DFS & BFS
대표적인 그래프 탐색 알고리즘

탐색이란 많은 양의 데이터중에서 원하는 데이터를 찾는 과정

스택 자료구조 - 선입후출
입구와 출구가 동일한 형태
'''

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 요소부터 출력
print(stack)

'''
큐자료구조 - 선입선출
입구와 출구가 모두 뚫려있는 터널과 같은 형태
'''
from collections import deque

#큐 구현을 위해 deque사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력

'''
재귀함수 - 자기자신을 호출하는 함수
함수가 스택에 쌓이고 실행됨
'''
def recursive_funtion(i):
    if i ==100: return
    print(i,"번째 재귀함수 호출",i+1,"번째 재귀함수를 호출합니다.")
    recursive_funtion(i+1)
    print(i,"번째 재귀함수를 종료합니다")

recursive_funtion(1)

'''
최대공약수(Greatest Common Divisor)
즉,gcd는 유클리드 호제법으로 구할수 있다
유클리드 호제법이란 A>B일때
A/B의 나머지를 R이라고 한다면
A,B의 최대 공약수는 B,R의 최대 공약수와 같다는것
'''

def gcd(a,b):
    if a%b ==0:
        return b
    else:
       return gcd(b,a%b)

print(gcd(192,162))

'''
재귀함수 유의사항
1.알고리즘을 간결하게 작성할 수 있으나 다른사람이 이해하기 어려울 수 있음
2.재귀함수로 구현이가능하다면 반복문으로 구현이가능함
3.재귀힘수과 반복문 항상 한쪽이 유리하지 않음
'''





'''
DFS(Depth-First Search)
깊이 우선 탐색 - 깊은 부분을 우선적으로 탐색
스택자료 혹은 재귀함수를 이용

동작과정
1.탐색시작노드를 스택에 삽입후 방문처리
2.최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그노드를 스택에 넣고 방문처리
  방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
3.더이상 2번을 수행할 수 없을때까지 반복
'''

#각 노드가 연결된 정보를 표현(2차원 리스트)
graph=[
[], # 0번째 노드는 없기 떄문에 계산의 간편함을 위해 비워두는 것이 좋음 
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False]*9 #여기도 실제 사용노드는 8개지만 0번째 임의의 노드 때문에 9로 설정

#DFS 메서드 정의
def dfs(graph,v,visited):
    #현재 노드 방문처리
    visited[v] =True
    print(v,end=" ")
    #현재노드와 연결된 다른노드 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)


'''
BFS(Breadth-First Search)
너비 우선 탐색 - 가까운 노드부터 우선적으로 탐색
큐 자료구조를 이용

동작과정
1.탐색시작노드를 큐에 삽입후 방문처리
2.큐에서 노드를 꺼낸뒤 해당 노드의 인접노드중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
3.더이상 2번을 수행할 수 없을때까지 반복
'''

#각 노드가 연결된 정보를 표현(2차원 리스트)
graph=[
[], # 0번째 노드는 없기 떄문에 계산의 간편함을 위해 비워두는 것이 좋음 
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False]*9 #여기도 실제 사용노드는 8개지만 0번째 임의의 노드 때문에 9로 설정

from collections import deque

def bfs(graph,start,visited):
    #Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아서 출력하기
        v= queue.popleft()
        print(v,end=" ")
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True

bfs(graph,1,visited)

#음료수 얼려 먹기
n,m= map(int,input().split())
graph =[]

for i in range(n):
    graph.append(list(map(int,input())))

#dfs로 특정 노드 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y]=1
        #상하좌우 재귀호출 -> 얼음은 부은곳 상하좌우가 한덩어리
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
    

#모든 위치에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True:
           result+=1 

print(result)


#미로 탈출
'''
BFS사용 -> BFS는 간선의 비용이 같을때 최단거리 탐색
'''
n,m= map(int,input().split())
graph =[]

for i in range(n):
    graph.append(list(map(int,input())))

#이동할  네가지 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def exit(x,y):
    queue = deque()
    queue.append(x,y)
    while queue:
        x,y=queue.popleft()
        #현재위치에서 4방향확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #미로를 벗어난 경우 무시
            if nx <0 or nx>=n or ny<0 or ny>=m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] ==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))

    
    



                
