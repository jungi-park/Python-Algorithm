def solution(numbers, target):
    answer = DFS(0,0,target,numbers)
    return answer

def DFS(x, sumVal, targetVal, numbers):
    if x == len(numbers):
        if sumVal == targetVal: 
            return 1
        else: 
            return 0
    else:
        return DFS(x + 1, sumVal + numbers[x], targetVal, numbers) + DFS(x + 1, sumVal - numbers[x], targetVal, numbers)

