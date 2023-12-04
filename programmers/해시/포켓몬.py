def solution(nums):
    answer = int(len(nums)/2)
    nums = set(nums)
    setNumsLen = len(nums)
    if answer > setNumsLen:
        return setNumsLen
    return answer