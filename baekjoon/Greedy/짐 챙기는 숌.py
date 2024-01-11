N, M = map(int, input().split())  # 책의 개수 N과 박스의 최대 무게 M을 입력받음
weights = list(map(int, input().split()))  # 책의 무게들을 입력받음

weights.sort()  # 책의 무게를 오름차순으로 정렬

count = 0  # 필요한 박스의 개수를 세기 위한 변수
current_weight = 0  # 현재 박스에 넣은 책들의 무게의 합을 저장하는 변수

for weight in weights:
    if current_weight + weight > M:  # 현재 책을 넣으면 최대 무게를 초과하면 새로운 박스에 넣어야 함
        count += 1
        current_weight = 0  # 새로운 박스에 넣을 때는 현재 무게를 초기화
    current_weight += weight  # 책을 현재 박스에 넣음

if current_weight > 0:  # 마지막 박스에 남은 책이 있는 경우
    count += 1

print(count)  # 필요한 박스의 개수 출력