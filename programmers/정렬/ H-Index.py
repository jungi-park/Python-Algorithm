def solution(citations):
    citations.sort(reverse=True)
# clitation    6,5,3,1,0 -> 인용횟수 저기서 말하는 h
# idx   0,1,2,3,4 ->  논문 갯수 n
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)