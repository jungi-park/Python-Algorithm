def solution(book_time):
    timelist = [0]
    times = []
    for time in book_time:
        imsi = []
        for i in time:
            x = "".join(map(str, i.split(":")))
            x = int(x[0:2]) *60 + int(x[2:])
            imsi.append(x)
        times.append(imsi)
    times.sort(key=lambda x: (x[0],x[1]))
    for inTime, outTime in times:
        flag = False
        for index, reserveTime in enumerate(timelist):
            if inTime >= reserveTime:
                timelist[index] = outTime + 10
                flag = True
                break
        if not flag:
            timelist.append(outTime + 10)
    return len(timelist)