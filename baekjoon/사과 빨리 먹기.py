# 문제풀이 실패

import sys

sys.setrecursionlimit(10**8)

graph = [list(map(int,input().split())) for _ in range(5)]

r,c = map(int,input().split())

d = [(1,0),(-1,0),(0,1),(0,-1)]

def DFS(sx,sy,apple,distance):
  min_distance = float("inf")
  if apple ==3:
     return distance
  for dx,dy in d:
        nx = sx+ dx
        ny = sy+ dy
        if 0<=nx<5 and 0<=ny<5 and graph[nx][ny] != -1:
          temp = graph[nx][ny]
          graph[nx][ny] = -1
          if temp ==1:
            min_distance = min(min_distance, DFS(nx,ny,apple+1,distance+1))
          else:
            min_distance = min(min_distance, DFS(nx,ny,apple,distance+1))
          graph[nx][ny] = temp
  return min_distance

result = DFS(r,c,0,0)

print(result)
