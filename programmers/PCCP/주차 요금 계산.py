import math
def solution(fees, records):
    answer = []
    history = {}
    for record in records:
        record = record.split()
        if record[2] =="IN":
            h,m = map(int,record[0].split(":"))
            if record[1] not in history:
                 history[record[1]] = []
            history[record[1]].append(h*60 + m)
        elif record[2] =="OUT":
            h,m = map(int,record[0].split(":"))
            history[record[1]].append(h*60 + m)
    
    history = sorted(history.items())
    for h in history:
        useTime = 0
        fee = 0
        while h[1]:
            e = 23*60 + 59
            s = h[1].pop(0)
            if h[1]:
                e = h[1].pop(0)
            useTime += e - s
        
        if useTime <= fees[0]:
            fee = fees[1]
        else:
            useTime = useTime - fees[0]
            fee = fees[1]
            fee += math.ceil(useTime/fees[2]) * fees[3]
        answer.append(fee)
    return answer