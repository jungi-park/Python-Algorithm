def solution(record):
    answer = []
    real = []
    room = dict()
    for re in record:
        re = re.split()
        if re[0] == "Enter":
            answer.append(re[1]+" "+"님이 들어왔습니다.")
            room[re[1]] = re[2]
        if re[0] == "Leave":
            answer.append(re[1]+" "+"님이 나갔습니다.")
        if re[0] == "Change":
            room[re[1]] = re[2]
    for i  in  answer:
        nick = i.split()
        real.append(room[nick[0]]+nick[1]+" "+nick[2])
    return real