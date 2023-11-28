def solution(n, computers):
    answer = 0
    for i in range(n):
        if 1 in computers[i]:
            answer += 1
            DFS(computers[i],computers,i,n)
    return answer

def DFS(computerArry,computers,num,n):
    for i in range(n):
        if computerArry[i] == 1:
            computers[num][i] = 0
            DFS(computers[i],computers,i,n)