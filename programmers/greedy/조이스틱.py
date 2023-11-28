def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
       # 실시간 좌우 조작
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 3가지 중 최단 경로를 갱신
        '''
        문자열 중간에 가장 긴 'A'로 연속된 것을 찾고, 그 'AAA...AAA' 문자열 기준
        왼쪽을 먼저 방문하는 거리와 오른쪽을 먼저 방문하는 거리, 
        그리고 일자로 쭉 가는 len(name) - 1 중 최솟값을 alpha를 이동하면서 저장하는 것이다.
        '''
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) -next)])
    answer += min_move
    return answer