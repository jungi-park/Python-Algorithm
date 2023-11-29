from itertools import permutations
def solution(numbers):
    strNumArry = list(map(int,numbers))
    
    # 가능한 모든 길이의 순열을 생성
    all_numbers = []
    for r in range(1, len(strNumArry) + 1):
        all_numbers += list(permutations(strNumArry, r))
    # 순열을 숫자로 변환
    all_numbers = [''.join(map(str, num)) for num in all_numbers if num[0] != 0]
    
    primeNumArry = [num for num in set(all_numbers) if is_prime_number(int(num)) and int(num) != 1]
    
    return len(primeNumArry)

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임