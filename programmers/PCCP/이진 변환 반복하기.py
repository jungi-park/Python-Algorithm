def solution(s):
    answer = [0,0]
    while s != "1":
        answer[1] += s.count("0")
        s = "".join([i for i in s if i != "0"])
        s= format(len(s), 'b')
        answer[0] += 1
            
    return answer