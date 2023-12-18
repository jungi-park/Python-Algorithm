# 내 풀이 정확성: 82.6
def solution(numbers):
    answer = []
    
    for index,number in enumerate(numbers):
        answer.append(-1)
        for i in range(index,len(numbers)):
            if number < numbers[i]:
                answer.pop()
                answer.append(numbers[i])
                break
        
    return answer

# 답
def solution(numbers):
    answer = [-1] * len(numbers)  # 초기값으로 -1로 채워진 리스트 생성
    stack = []  # 인덱스를 저장할 스택

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]

        stack.append(i)
    
    return answer