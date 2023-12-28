def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-9):
        check = 0
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) == number[j]:
                check +=1
        if check == len(want):
            answer+=1
    return answer