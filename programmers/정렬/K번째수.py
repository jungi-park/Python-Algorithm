def solution(array, commands):
    answer = []
    for i,j,k in commands:
        sliceArry = array[i-1:j]
        sliceArry.sort()

        answer.append(sliceArry[k-1])
    return answer