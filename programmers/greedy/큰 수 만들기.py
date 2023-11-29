# 내답안 10개중 8개 통과 2개 시간초과
def solution(number, k):
    answer = ""
    numArry = list(map(int,number))
    makeLen = len(number)-k
    while makeLen != 0 and numArry:
        max_num = max(numArry[:len(numArry)-makeLen+1])
        answer += str(max_num)
        index = numArry.index(max_num)
        numArry = numArry[index+1:]
        makeLen -=1
    return answer

# 스택을 이용한 답안
def solution(number, k):
    stack = []
    for num in number:
      # 스택의 마지막 값이 새로운 값보다 작으면 없애고 지울수 있는기회(k)를 -1
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
      # for 문을 돌며 숫자 추가
        stack.append(num)
    # 모든 숫자를 처리한 후에도 제거해야 할 숫자가 남은 경우, 스택의 마지막에서 k개의 요소를 제거하는 역할을 합니다.
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
