def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    
    people.sort()  # 사람들의 몸무게를 오름차순으로 정렬
    
    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람의 몸무게를 비교
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람과 함께 태움
        right -= 1  # 가장 무거운 사람은 항상 태움
        
        answer += 1  # 구명보트의 개수 증가
    
    return answer